from pathlib import Path
import re


def replace_once(path: str, old: str, new: str, label: str) -> None:
    file = Path(path)
    source = file.read_text(encoding="utf-8")
    count = source.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected one match, got {count}")
    file.write_text(source.replace(old, new, 1), encoding="utf-8")


html = Path("website/index.html")
source = html.read_text(encoding="utf-8")
old = '''          <div class="hero-label" data-reveal>Version 2.1.1 · MIT · Windows, macOS, and Linux</div>
          <div class="hero-copy" data-reveal>
            <p class="hero-kicker">Desktop multi-provider AI gateway</p>
            <h1 id="hero-title">Use your AI providers through one local gateway.</h1>
            <p class="hero-description">
              Connect Claude, Codex, Z.ai, and other supported providers. Proxy-Inator gives local clients OpenAI-compatible and Anthropic-compatible routes.
            </p>
            <p class="hero-description">
              It selects routes, changes routes before output starts, and records usage on your computer.
            </p>
            <div class="hero-actions" role="group" aria-label="Start or download">
              <a class="button button-primary" href="docs/quick_start/" aria-label="Open the quick start guide">Quick start</a>
              <a class="button button-secondary" href="https://github.com/surajmandalcell/subscription-proxy-inator/releases/latest" aria-label="Download the latest desktop release">Download latest</a>
            </div>
            <p class="hero-assurance">The server listens on loopback by default. The app does not need a hosted control plane.</p>
          </div>

          <figure class="hero-system" aria-labelledby="hero-system-title hero-system-caption" data-reveal>
            <figcaption>
              <span class="diagram-eyebrow">Subscription routing</span>
              <strong id="hero-system-title">Connect providers once. Use them in many clients.</strong>
              <p id="hero-system-caption">Configured subscriptions enter Proxy-Inator. Local clients use one compatible API.</p>
            </figcaption>'''
new = '''          <div class="hero-copy" data-reveal>
            <p class="hero-kicker">Local AI gateway</p>
            <h1 id="hero-title">One local API for Claude, Codex, and Z.ai.</h1>
            <p class="hero-description">Proxy-Inator routes requests from your tools to configured provider accounts.</p>
            <div class="hero-actions" role="group" aria-label="Get started">
              <a class="button button-primary" href="docs/quick_start/" aria-label="Open the quick start guide">Quick start</a>
              <a class="button button-secondary" href="https://github.com/surajmandalcell/subscription-proxy-inator/releases/latest" aria-label="Download the latest desktop release">Download latest</a>
            </div>
          </div>

          <figure class="hero-system" aria-labelledby="hero-system-title" data-reveal>
            <figcaption>
              <span class="diagram-eyebrow">Request flow</span>
              <strong id="hero-system-title">Subscriptions in. Local clients out.</strong>
            </figcaption>'''
count = source.count(old)
if count != 1:
    raise SystemExit(f"hero block: expected one match, got {count}")
source = source.replace(old, new, 1)

replacements = [
    ('''                <div class="diagram-node">
                  <span>Subscription</span>
                  <strong>Claude</strong>
                  <small>Anthropic adapter</small>
                </div>''', '''                <div class="diagram-node"><strong>Claude</strong></div>''', "Claude node"),
    ('''                <div class="diagram-node">
                  <span>Subscription</span>
                  <strong>Codex</strong>
                  <small>Command adapter</small>
                </div>''', '''                <div class="diagram-node"><strong>Codex</strong></div>''', "Codex node"),
    ('''                <div class="diagram-node">
                  <span>Subscription</span>
                  <strong>Z.ai</strong>
                  <small>Compatible HTTP adapter</small>
                </div>''', '''                <div class="diagram-node"><strong>Z.ai</strong></div>''', "Z.ai node"),
    ('''                <span>Local gateway</span>
                <strong>Proxy-Inator</strong>
                <small>Routes requests and records usage</small>''', '''                <strong>Proxy-Inator</strong>
                <small>Local API</small>''', "hub text"),
    ('''                <div class="diagram-node">
                  <span>Developer tool</span>
                  <strong>Harness</strong>
                  <small>Compatible client</small>
                </div>''', '''                <div class="diagram-node"><strong>Harness</strong></div>''', "Harness node"),
    ('''                <div class="diagram-node">
                  <span>Workflow</span>
                  <strong>Automation</strong>
                  <small>Scheduled or event-driven</small>
                </div>''', '''                <div class="diagram-node"><strong>Automation</strong></div>''', "Automation node"),
    ('''                <div class="diagram-node">
                  <span>Product</span>
                  <strong>App</strong>
                  <small>Your local integration</small>
                </div>''', '''                <div class="diagram-node"><strong>App</strong></div>''', "App node"),
    ('''          <span>MIT License</span>''', '''          <span>Version 2.1.1 · MIT License</span>''', "footer version"),
]
for old_item, new_item, label in replacements:
    item_count = source.count(old_item)
    if item_count != 1:
        raise SystemExit(f"{label}: expected one match, got {item_count}")
    source = source.replace(old_item, new_item, 1)
html.write_text(source, encoding="utf-8")

css = Path("website/assets/polish.css")
source = css.read_text(encoding="utf-8")
css_replacements = [
    ('''.hero .site-grid {
  min-height: 760px;
  grid-template-rows: auto 1fr;
  row-gap: 24px;
}''', '''.hero .site-grid {
  min-height: 640px;
  align-items: center;
}''', "hero grid"),
    ('''.hero-description {
  max-width: 720px !important;
  margin-top: 28px !important;
}''', '''.hero-description {
  max-width: 600px !important;
  margin-top: 24px !important;
}''', "hero description"),
    ('''  gap: 16px;
  margin-top: 40px;
}''', '''  gap: 16px;
  margin-top: 32px;
}''', "hero actions"),
    ('''.hero-assurance {
  max-width: 680px !important;
  margin-top: 24px !important;
  color: var(--gray-40) !important;
  font-size: 14px !important;
  line-height: 20px !important;
}

''', "", "hero assurance CSS"),
    ('''  min-height: 420px;
  display: grid;
  grid-template-columns: minmax(132px, 1fr) 148px minmax(132px, 1fr);
  align-items: center;
  gap: 48px;
  padding: 18px 0 20px;''', '''  min-height: 360px;
  display: grid;
  grid-template-columns: minmax(132px, 1fr) 148px minmax(132px, 1fr);
  align-items: center;
  gap: 48px;
  padding: 16px 0;''', "diagram geometry"),
    ('''.diagram-node {
  min-height: 88px;
  display: grid;
  align-content: center;
  gap: 2px;
  padding: 14px 16px;
  border: 1px solid var(--gray-60);
  background: var(--gray-100);
}''', '''.diagram-node {
  min-height: 64px;
  display: grid;
  place-items: center;
  padding: 16px;
  border: 1px solid var(--gray-60);
  background: var(--gray-100);
  text-align: center;
}''', "diagram node"),
    ('''.diagram-node > span {
  color: var(--gray-40);
  font-family: "IBM Plex Mono", ui-monospace, monospace;
  font-size: 10px;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}

''', "", "node label CSS"),
    ('''.diagram-node small {
  color: var(--gray-30);
  font-size: 12px;
  line-height: 16px;
}

''', "", "node detail CSS"),
    ('''.diagram-hub {
  min-height: 244px;''', '''.diagram-hub {
  min-height: 208px;''', "hub geometry"),
    ('''.diagram-hub span {
  color: #d0e2ff;
  font-family: "IBM Plex Mono", ui-monospace, monospace;
  font-size: 10px;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

''', "", "hub label CSS"),
    ('''    min-height: 400px;
    grid-template-columns: minmax(140px, 1fr) 160px minmax(140px, 1fr);''', '''    min-height: 340px;
    grid-template-columns: minmax(140px, 1fr) 160px minmax(140px, 1fr);''', "tablet diagram"),
]
for old_item, new_item, label in css_replacements:
    item_count = source.count(old_item)
    if item_count != 1:
        raise SystemExit(f"{label}: expected one match, got {item_count}")
    source = source.replace(old_item, new_item, 1)
css.write_text(source, encoding="utf-8")

tests = Path("tests/repository/interface-completion.test.js")
source = tests.read_text(encoding="utf-8")
pattern = re.compile(r"test\('the hero explains[\s\S]*?\n\}\);\n\n(?=test\('one white calendar-refresh glyph)")
replacement = '''test('the hero uses one concise message and one routing diagram', async () => {
  const html = await text('website/index.html');
  const styles = await text('website/assets/polish.css');

  assert.match(html, /One local API for Claude, Codex, and Z\.ai\./);
  assert.match(html, /Proxy-Inator routes requests from your tools to configured provider accounts\./);
  assert.equal((html.match(/class="hero-description"/g) ?? []).length, 1);
  assert.doesNotMatch(html, /hero-label|hero-assurance/);
  assert.match(html, /class="hero-system"/);
  assert.match(html, /class="system-diagram"/);
  assert.match(html, /Claude[\s\S]*Codex[\s\S]*Z\.ai[\s\S]*Proxy-Inator[\s\S]*Harness[\s\S]*Automation[\s\S]*App/);
  assert.match(html, /aria-label="Claude, Codex, and Z\.ai connect to Proxy-Inator/);
  assert.match(html, /class="hero-actions" role="group" aria-label="Get started"/);
  assert.match(styles, /\.hero \.site-grid\s*\{[\s\S]*min-height:\s*640px/);
  assert.match(styles, /\.hero-actions\s*\{[\s\S]*gap:\s*16px/);
  assert.match(styles, /\.hero-actions\s*\{[\s\S]*margin-top:\s*32px/);
  assert.match(styles, /\.hero-actions \.button[\s\S]*min-inline-size:\s*168px/);
  assert.match(styles, /\.diagram-node\s*\{[\s\S]*min-height:\s*64px/);
  assert.match(styles, /\.button:focus-visible[\s\S]*outline:\s*3px solid/);
});

'''
source, count = pattern.subn(replacement, source, count=1)
if count != 1:
    raise SystemExit(f"hero test: expected one match, got {count}")
tests.write_text(source, encoding="utf-8")

replace_once(
    "docs/DESIGN_SYSTEM.md",
    '''The first viewport must identify these facts:

1. The product is a desktop multi-provider AI gateway.
2. The product gives clients one local compatible API.
3. The product routes requests and records usage.
4. Failover stops after visible output starts.
5. The system diagram shows sources, Proxy-Inator, and clients.
6. Quick start and Download are separate actions.

The diagram uses Claude, Codex, and Z.ai as configured source examples.

Claude uses the Anthropic adapter. Codex uses a command adapter. Z.ai uses a compatible HTTP adapter.

Harness, Automation, and App are example local clients. They are not live user data.''',
    '''The first viewport must use one headline, one descriptive sentence, two actions, and one system diagram.

The headline identifies the local API. The sentence identifies the routing function.

The diagram shows Claude, Codex, and Z.ai as example sources. It shows Harness, Automation, and App as example local clients.

Quick start and Download are separate actions. Do not add a version strip, assurance paragraph, adapter labels, or client descriptions to the hero.''',
    "website hierarchy",
)

changelog = Path("CHANGELOG.md")
source = changelog.read_text(encoding="utf-8")
marker = "### Technical writing\n\n"
addition = '''### Documentation cleanup

- Removed the Version 1 migration page.
- Removed the public writing-profile page. The automated ASD-STE100 gate remains active.
- Reduced the hero to one headline, one sentence, two actions, and the routing diagram.

'''
if addition not in source:
    marker_count = source.count(marker)
    if marker_count != 1:
        raise SystemExit(f"changelog marker: expected one match, got {marker_count}")
    source = source.replace(marker, addition + marker, 1)
changelog.write_text(source, encoding="utf-8")
