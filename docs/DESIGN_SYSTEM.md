# Interface design system

## Scope

The desktop renderer, website, and generated docs use one visual system.

The design uses IBM Plex and guidance from IBM 2x Grid and Carbon. The project is not affiliated with or endorsed by IBM.

## Product icon

The product icon is a blue rounded square. It contains one white calendar and refresh glyph.

Rules:

- The website, renderer, and build SVG files must be identical.
- The glyph uses white only.
- The SVG is the primary icon source.
- `build/icon.png` is a generated 1024 px package icon.
- Web PNG icons are generated from the same SVG.
- The web manifest uses 192 px and 512 px PNG alternatives.
- The icon must have an even optical margin.
- The refresh mark must remain clear at small sizes.
- Do not keep a retired icon source in the repository.

## Type

- Use IBM Plex Sans for interface text.
- Use IBM Plex Mono for routes, IDs, logs, JSON, and shell commands.
- Load the typefaces from pinned local packages.
- Do not reduce important text to fit a small window.

## Spacing

Use a 4 px base and an 8 px main rhythm.

| Token | Value | Use |
| --- | ---: | --- |
| `spacing-01` | 2 px | Optical correction |
| `spacing-02` | 4 px | Tight icon or label gap |
| `spacing-03` | 8 px | Inline control gap |
| `spacing-04` | 12 px | Compact padding |
| `spacing-05` | 16 px | Standard padding |
| `spacing-06` | 24 px | Panel gap |
| `spacing-07` | 32 px | Page gutter |
| `spacing-08` | 40 px | Compact page gap |
| `spacing-09` | 48 px | Main section gap |
| `spacing-10` | 64 px | Wide section gap |

Use a 16-column grid on wide screens. Change the column count at defined breakpoints.

Use at least 16 px between adjacent calls to action. Use at least 12 px when the actions stack.

Use equal columns for wide split sections unless the information needs a different ratio.

## Geometry and alignment

- Make primary desktop controls at least 40 px high.
- Make website calls to action at least 48 px high.
- Make mobile navigation targets at least 48 px high.
- Use square or small-radius surfaces.
- Align action groups to one baseline.
- Wrap the complete action group before controls become crowded.
- Use shared tokens for gutters, padding, headings, and form gaps.
- Use borders and background layers for hierarchy.
- Do not use glass effects or decorative glows.
- Use color for a defined state or action.

## Website hierarchy

The first viewport must use one headline, one descriptive sentence, two actions, and one system diagram.

The headline identifies the local API. The sentence identifies the routing function.

The diagram shows Claude, Codex, and Z.ai as example sources. It shows Harness, Automation, and App as example local clients.

Quick start and Download are separate actions. Do not add a version strip, assurance paragraph, adapter labels, or client descriptions to the hero.

Do not show false traffic, cost, latency, user, or account values.

## Desktop layout

The desktop shell has these areas:

1. A 48 px titlebar
2. A 256 px side navigation on wide screens
3. A scrollable content area

Responsive rules:

- At 1320 px, dense editors use fewer columns.
- At 1040 px, two-column pages use one column.
- At 1040 px, the side navigation becomes an icon rail.
- At 800 px, page actions stack.
- At 800 px, data filters use two columns.
- At 620 px, forms and strategy cards use one column.

Windows, macOS, and Linux use the same DOM and breakpoints.

## Motion

Use motion only to show a state or direction.

- Use about 120 ms for color and border changes.
- Use 180 through 260 ms for page and notice changes.
- Keep movement at 16 px or less.
- Keep hover movement at 2 px or less.
- Reveal a website section one time.
- Move diagram dashes slowly to show direction.
- Keep diagram labels static.
- Use a short page fade in the desktop app.
- Remove nonessential motion when Reduce motion is on.
- Respect the operating-system reduced-motion setting.

## Accessibility

- Give each control a visible 3 px focus indicator.
- Do not use color as the only status signal.
- Keep visible labels on form fields.
- Give the hero diagram a complete text alternative.
- Update `aria-expanded` for mobile navigation.
- Move focus into an open mobile menu.
- Close the menu with Escape.
- Return focus to the menu button.
- Announce copy success or failure.
- Permit horizontal table scrolling.
- Give each icon-only control an accessible name.

## Maintenance

Update a repository test when a design rule changes. Use existing tokens before you add a new value.

Do not add marketing claims, false metrics, or unsupported functions.
