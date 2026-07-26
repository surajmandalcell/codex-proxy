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
    new = """    if count != 1:
        if path == 'desktop/renderer/pages/Providers.jsx' and 'setDraft(provider)' in old:
            return
        raise SystemExit(f'{path}: expected one match, found {count}: {old[:100]!r}')
"""
    if old not in text:
        raise SystemExit('replace_once helper was not found in extracted patch script')
    path.write_text(text.replace(old, new, 1), encoding='utf-8')
elif mode == 'finish':
    path = Path('desktop/renderer/pages/Providers.jsx')
    text = path.read_text(encoding='utf-8')
    text, count = re.subn(
        r"onClick=\{\(\) => \{\s*setDraft\(provider\);\s*setHeadersText\(pretty\(provider\.headers\)\);\s*setAdapterText\(pretty\(provider\.adapter\)\);\s*\}\}",
        'onClick={reset}',
        text,
        count=1,
    )
    if count != 1:
        raise SystemExit(f'provider discard handler replacement count: {count}')
    path.write_text(text, encoding='utf-8')
else:
    raise SystemExit(f'Unknown mode: {mode}')
