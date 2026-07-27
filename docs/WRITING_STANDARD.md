# ASD-STE100 writing profile

## Status

This project uses ASD-STE100 Simplified Technical English, Issue 9, as its writing basis.

ASD-STE100 is an international standard for technical documentation. ASD owns the standard.

This repository does not claim ASD certification. The project checker applies a defined subset and project technical terms.

## Purpose

Use this profile for these files:

- `README.md`
- Root policy and contribution files
- Markdown files in `docs/`
- Public website text
- Issue and pull-request templates

## Project rules

1. Use short sentences.
2. Use one topic in each sentence.
3. Use active voice when the actor is important.
4. Use the present tense for system behavior.
5. Use the imperative form for an instruction.
6. Put one action in each numbered step.
7. Use a maximum of 20 words in an instruction.
8. Use a maximum of 25 words in a descriptive sentence.
9. Use the same word for the same function.
10. Do not use contractions.
11. Do not use semicolons in prose.
12. Do not use marketing words or unsupported claims.
13. Define an abbreviation before repeated use, unless it is a protocol name.
14. Keep code, routes, field names, and product names unchanged.

## Approved technical terms

The project uses technical nouns that are not general STE words. Examples include:

- API
- account
- adapter
- alias
- Anthropic
- cache
- Claude
- Codex
- configuration
- credential
- Electron
- endpoint
- failover
- Fastify
- Gemini
- Grok
- HTTP
- JSON
- loopback
- model
- OpenAI
- provider
- Proxy-Inator
- renderer
- route
- routing
- SQLite
- stream
- token
- tool call
- vault
- Z.ai

The project can add a technical noun when no approved general word gives the correct meaning.

## Prohibited phrases

Do not use these phrases in public technical text:

- `and/or`
- `in order to`
- `prior to`
- `subsequent to`
- `utilize`
- `leverage`
- `seamless`
- `powerful`
- `robust`
- `easy to use`
- `simply`
- `obviously`

Use a direct alternative. For example, use `before` instead of `prior to`.

## Automated check

Run this command:

```bash
npm run check:ste
```

The checker removes code blocks and markup before it checks prose. It reports long sentences, contractions, semicolons, and prohibited phrases.

The checker cannot replace technical review. A reviewer must confirm accuracy, active voice, one topic per sentence, and consistent terminology.

## Source

The current standard is ASD-STE100 Issue 9, dated 2025-01-15. Request the official copy from the ASD STEMG website.
