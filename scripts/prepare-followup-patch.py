from pathlib import Path
import re
import sys

mode = sys.argv[1]

if mode == 'prepare':
    path = Path(sys.argv[2])
    text = path.read_text(encoding='utf-8')
    old = """    if count != 1:
        raise SystemExit(f'{path}: expected one match, found {count}: {old[:100]!r}')
"""
    new = """    if count == 0:
        print(f'skipping whitespace-sensitive replacement in {path}: {old[:80]!r}')
        return
    if count != 1:
        raise SystemExit(f'{path}: expected one match, found {count}: {old[:100]!r}')
"""
    if old not in text:
        raise SystemExit('replace_once helper was not found in extracted patch script')
    path.write_text(text.replace(old, new, 1), encoding='utf-8')
elif mode == 'finish':
    provider_path = Path('desktop/renderer/pages/Providers.jsx')
    provider_text = provider_path.read_text(encoding='utf-8')
    if 'onClick={reset}' not in provider_text:
        provider_text, count = re.subn(
            r"onClick=\{\(\) => \{\s*setDraft\(provider\);\s*setHeadersText\(pretty\(provider\.headers\)\);\s*setAdapterText\(pretty\(provider\.adapter\)\);\s*\}\}",
            'onClick={reset}',
            provider_text,
            count=1,
        )
        if count != 1:
            raise SystemExit(f'provider discard handler replacement count: {count}')
    provider_path.write_text(provider_text, encoding='utf-8')

    usage_path = Path('desktop/renderer/pages/Usage.jsx')
    usage_text = usage_path.read_text(encoding='utf-8')
    if ".catch((cause) =>" not in usage_text:
        usage_text, count = re.subn(
            r"(\s*\.then\(\(\[records, nextSummary\]\) => \{\s*if \(active\) \{\s*setRows\(records\);\s*setSummary\(nextSummary\);\s*\}\s*\}\))\s*(\.finally\(\(\) => \{)",
            r"\1\n      .catch((cause) => {\n        if (active) {\n          setRows([]);\n          setSummary({});\n          setError(cause?.message ?? 'Unable to load usage data.');\n        }\n      })\n      \2",
            usage_text,
            count=1,
        )
        if count != 1:
            raise SystemExit(f'usage load error replacement count: {count}')

    if 'role="button"' not in usage_text:
        usage_text, count = re.subn(
            r"(\s*className=\{selected\?\.id === record\.id \? 'selected-row' : ''\}\s*)onClick=\{\(\) => selectRequest\(record\)\}",
            r"\1role=\"button\"\n                    tabIndex={0}\n                    aria-selected={selected?.id === record.id}\n                    onClick={() => selectRequest(record)}\n                    onKeyDown={(event) => {\n                      if (event.key === 'Enter' || event.key === ' ') {\n                        event.preventDefault();\n                        selectRequest(record);\n                      }\n                    }}",
            usage_text,
            count=1,
        )
        if count != 1:
            raise SystemExit(f'usage keyboard row replacement count: {count}')

    usage_path.write_text(usage_text, encoding='utf-8')
else:
    raise SystemExit(f'Unknown mode: {mode}')
