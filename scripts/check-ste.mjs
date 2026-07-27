import { readFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import process from 'node:process';

const root = path.resolve(import.meta.dirname, '..');
const fixedFiles = [
  'README.md',
  'CHANGELOG.md',
  'CODE_OF_CONDUCT.md',
  'CONTRIBUTING.md',
  'SECURITY.md',
  'SUPPORT.md',
  '.github/pull_request_template.md',
  '.github/ISSUE_TEMPLATE/bug.yml',
  '.github/ISSUE_TEMPLATE/feature.yml',
  '.github/ISSUE_TEMPLATE/config.yml',
  'website/index.html',
  'website/404.html',
  'website/manifest.webmanifest',
  'package.json',
];

async function walkMarkdown(directory) {
  const output = [];
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const absolute = path.join(directory, entry.name);
    if (entry.isDirectory()) output.push(...await walkMarkdown(absolute));
    if (entry.isFile() && entry.name.endsWith('.md')) output.push(path.relative(root, absolute));
  }
  return output;
}

const prohibited = [
  'and/or',
  'in order to',
  'prior to',
  'subsequent to',
  'utilize',
  'leverage',
  'seamless',
  'powerful',
  'robust',
  'easy to use',
  'simply',
  'obviously',
  'very',
  'basically',
];

const contractions = /\b(?:aren't|can't|couldn't|didn't|doesn't|don't|hasn't|haven't|isn't|it's|shouldn't|that's|they're|wasn't|weren't|won't|wouldn't|you're)\b/i;
const wordPattern = /[A-Za-z0-9]+(?:[.'_-][A-Za-z0-9]+)*/g;

function decodeEntities(value) {
  return value
    .replaceAll('&amp;', '&')
    .replaceAll('&lt;', '<')
    .replaceAll('&gt;', '>')
    .replaceAll('&quot;', '"')
    .replaceAll('&#39;', "'")
    .replace(/&#(\d+);/g, (_, number) => String.fromCodePoint(Number(number)));
}

function removeInlineCode(value) {
  return value
    .replace(/`[^`]*`/g, ' TECHNICAL_TERM ')
    .replace(/!\[[^\]]*\]\([^)]*\)/g, ' ')
    .replace(/\[([^\]]+)\]\([^)]*\)/g, '$1')
    .replace(/https?:\/\/\S+/g, ' URL ')
    .replace(/[*_~]/g, ' ');
}

function markdownSegments(source) {
  const segments = [];
  let inFence = false;
  let paragraph = [];

  const flush = () => {
    if (paragraph.length) segments.push({ text: paragraph.join(' '), instruction: false });
    paragraph = [];
  };

  for (const rawLine of source.split(/\r?\n/)) {
    const line = rawLine.trim();
    if (line.startsWith('```')) {
      flush();
      inFence = !inFence;
      continue;
    }
    if (inFence || !line) {
      flush();
      continue;
    }
    if (/^#{1,6}\s/.test(line) || /^\|/.test(line) || /^[-:| ]+$/.test(line)) {
      flush();
      continue;
    }
    const numbered = line.match(/^\d+[.)]\s+(.*)$/);
    if (numbered) {
      flush();
      segments.push({ text: numbered[1], instruction: true });
      continue;
    }
    const bullet = line.match(/^[-*+]\s+(.*)$/);
    if (bullet) {
      flush();
      segments.push({ text: bullet[1], instruction: false });
      continue;
    }
    paragraph.push(line);
  }
  flush();
  return segments;
}

function htmlSegments(source) {
  const clean = source
    .replace(/<script[\s\S]*?<\/script>/gi, ' ')
    .replace(/<style[\s\S]*?<\/style>/gi, ' ')
    .replace(/<svg[\s\S]*?<\/svg>/gi, ' ')
    .replace(/<pre[\s\S]*?<\/pre>/gi, ' ')
    .replace(/<code[\s\S]*?<\/code>/gi, ' TECHNICAL_TERM ');
  const output = [];
  for (const match of clean.matchAll(/>([^<>]+)</g)) {
    const text = decodeEntities(match[1]).trim();
    if (text) output.push({ text, instruction: false });
  }
  for (const match of source.matchAll(/\b(?:content|aria-label|alt|title)="([^"]+)"/g)) {
    const text = decodeEntities(match[1]).trim();
    if (text) output.push({ text, instruction: false });
  }
  return output;
}

function yamlSegments(source) {
  const output = [];
  for (const rawLine of source.split(/\r?\n/)) {
    const line = rawLine.trim();
    if (!line || line.startsWith('#')) continue;
    const match = line.match(/^(?:name|description|about|label|placeholder|value):\s*(.+)$/);
    if (match) output.push({ text: match[1].replace(/^['"]|['"]$/g, ''), instruction: false });
  }
  return output;
}

function jsonSegments(source) {
  const data = JSON.parse(source);
  const output = [];
  const collect = (value, key = '') => {
    if (typeof value === 'string') {
      if (['description', 'name', 'short_name'].includes(key)) output.push({ text: value, instruction: false });
      return;
    }
    if (Array.isArray(value)) return value.forEach((item) => collect(item, key));
    if (value && typeof value === 'object') {
      for (const [childKey, child] of Object.entries(value)) collect(child, childKey);
    }
  };
  collect(data);
  return output;
}

function splitSentences(text) {
  const normalized = removeInlineCode(text).replace(/\s+/g, ' ').trim();
  if (!normalized) return [];
  return normalized.split(/(?<=[.!?])\s+(?=[A-Z0-9])/).map((item) => item.trim()).filter(Boolean);
}

function checkSegment(file, segment, errors) {
  const prose = removeInlineCode(segment.text);
  const lower = prose.toLowerCase();
  for (const phrase of prohibited) {
    if (lower.includes(phrase)) errors.push(`${file}: prohibited phrase ${JSON.stringify(phrase)} in: ${segment.text}`);
  }
  if (contractions.test(prose)) errors.push(`${file}: contraction in: ${segment.text}`);
  if (prose.includes(';')) errors.push(`${file}: semicolon in prose: ${segment.text}`);

  for (const sentence of splitSentences(segment.text)) {
    const words = sentence.match(wordPattern) ?? [];
    const limit = segment.instruction ? 20 : 25;
    if (words.length > limit) errors.push(`${file}: ${words.length}-word sentence exceeds ${limit}: ${sentence}`);
  }
}

const docs = await walkMarkdown(path.join(root, 'docs'));
const files = [...new Set([...fixedFiles, ...docs])].sort();
const errors = [];
let segmentCount = 0;

for (const file of files) {
  const source = await readFile(path.join(root, file), 'utf8');
  let segments;
  if (file.endsWith('.html')) segments = htmlSegments(source);
  else if (file.endsWith('.yml') || file.endsWith('.yaml')) segments = yamlSegments(source);
  else if (file.endsWith('.json') || file.endsWith('.webmanifest')) segments = jsonSegments(source);
  else segments = markdownSegments(source);
  segmentCount += segments.length;
  for (const segment of segments) checkSegment(file, segment, errors);
}

if (errors.length) {
  console.error(`ASD-STE100 project profile failed with ${errors.length} issue(s).`);
  for (const error of errors) console.error(`- ${error}`);
  process.exit(1);
}

console.log(`ASD-STE100 project profile passed for ${files.length} files and ${segmentCount} text segments.`);
