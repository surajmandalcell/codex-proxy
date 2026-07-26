# Interface design system

## Scope

The desktop renderer, product website, and generated documentation use one visual contract. The implementation is inspired by IBM Plex, IBM's public 2x Grid guidance, and Carbon's spacing and interaction principles. Subscription Proxy Inator is not affiliated with or endorsed by IBM.

## Product icon

The canonical mark is a balanced rounded-square icon containing a calendar with a refresh badge in the bottom-right corner. The calendar represents subscription and usage periods; the refresh badge represents routing, retry, and provider switching.

- `website/assets/icon.svg`, `desktop/renderer/assets/icon.svg`, and `build/icon.svg` must remain identical.
- The SVG is the source for the favicon, website header, desktop shell, boot state, web manifest, and Electron packaging on Windows, macOS, and Linux.
- The mark must retain an even optical margin, rounded outer corners, and a high-contrast refresh badge at small sizes.
- Retired raster icon sources must not remain in the repository after the SVG source becomes canonical.

## Typography

- IBM Plex Sans is the interface typeface at weights 300, 400, 500, and 600.
- IBM Plex Mono is used for routes, identifiers, logs, configuration JSON, and shell commands.
- The desktop renderer imports pinned local Fontsource packages. The website generator copies the same pinned font files into the static site.
- Primary interface text does not shrink to fit smaller windows. Layout changes before typography becomes unreadable.

## Spacing and grid

The token scale uses a Carbon-like 4 px base with an 8 px major layout rhythm. Optical adjustments may use 2 px; component and section spacing primarily use 8 px multiples:

| Token | Value | Primary use |
| --- | ---: | --- |
| `spacing-01` | 2 px | Hairline optical adjustment |
| `spacing-02` | 4 px | Tight label and icon spacing |
| `spacing-03` | 8 px | Inline control spacing |
| `spacing-04` | 12 px | Compact internal padding |
| `spacing-05` | 16 px | Standard component padding |
| `spacing-06` | 24 px | Section and panel spacing |
| `spacing-07` | 32 px | Page gutters and large gaps |
| `spacing-08` | 40 px | Compact page transitions |
| `spacing-09` | 48 px | Major section spacing |
| `spacing-10` | 64 px | Wide-screen section spacing |

The website and desktop page headers use a 16-column grid at wide sizes. Components collapse into fewer columns at defined breakpoints rather than using arbitrary widths.

CTA groups use at least 16 px between adjacent actions on standard layouts and at least 12 px when stacked on narrow screens. Adjacent actions must remain visually separate; one-pixel seams are reserved for data grids, not primary actions.

## Geometry and alignment

- Primary controls are at least 40 px high; public website CTAs are at least 48 px high.
- Table rows and navigation targets are at least 40 px high; mobile navigation targets are at least 48 px high.
- Panels, fields, tables, and navigation use square or minimally rounded geometry.
- Action groups align to the same baseline and wrap as a group before controls become cramped.
- Page gutters, panel padding, heading spacing, and form gaps use shared tokens rather than one-off values.
- Borders and layer changes establish hierarchy. Gradients, glass surfaces, ambient glows, and decorative shadows are not part of the system.
- Color is functional: blue for primary action/selection, green for success, yellow for warning, and red for destructive/error states.

## Website information hierarchy

The first viewport must explain the application without requiring scrolling. It contains:

1. The product category: desktop multi-provider AI gateway.
2. The primary outcome: one local API for multiple AI providers.
3. The factual behavior: account eligibility, routing, pre-stream failover, and local usage accounting.
4. A client → local gateway → provider request path.
5. Separate Quick start and Download actions.

The website contains only project facts and direct actions. It does not display fabricated traffic, cost, latency, availability, user, or account data. Remaining sections document implemented capabilities, provider adapters, routing strategies, exact local HTTP routes, security boundaries, and build links.

## Desktop structure

The desktop shell has three stable regions:

1. A 48 px custom titlebar containing product identity, gateway state, and window controls.
2. A 256 px side navigation at wide and medium widths.
3. A scrollable content region with a bounded maximum width and responsive grid.

Responsive behavior:

- At 1320 px and below, high-density editors use fewer columns.
- At 1040 px and below, two-column page layouts become one column and the side navigation becomes an icon rail.
- At 800 px and below, page headers and actions stack, data filters use two columns, and wide tables scroll horizontally.
- At 620 px and below, form grids and strategy cards become one column while titlebar controls remain reachable.

The renderer does not expose separate platform-specific page layouts. macOS, Windows, and Linux use the same DOM, tokens, sizes, and breakpoints.

## Motion

Motion is limited to opacity, color, and short spatial transitions that explain state or navigation changes.

- Interactive color and border transitions use approximately 120 ms.
- Page, notice, and reveal transitions use approximately 180–260 ms.
- Spatial movement is limited to 16 px or less and must not block input.
- Hover movement is limited to 1–2 px and cannot be the only indication of interactivity.
- Website sections reveal once as they enter the viewport; they do not loop or animate while reading.
- Desktop page changes use a short fade and vertical settle; loading and error layers use short opacity/position transitions.
- The application Reduce motion preference and the operating-system `prefers-reduced-motion` setting both remove nonessential animation and smooth scrolling.

## Accessibility

- All interactive controls have visible 3 px focus indicators with sufficient contrast.
- Color is not the only status indicator; status text is always present.
- Form inputs retain visible labels and helper text.
- Mobile navigation maintains `aria-expanded`, moves focus to the opened menu, closes on Escape, and restores focus to the trigger.
- Copy actions announce success or failure without removing their accessible name.
- Horizontal scrolling is allowed for dense tables instead of compressing columns below usable widths.
- Icon-only controls have explicit accessible labels; decorative product icons are hidden from assistive technology when adjacent text provides the name.

## Maintenance rules

A visual change must update tests when it changes a design contract. New components must use existing spacing, type, color, motion, and responsive tokens before introducing new values. Marketing copy, fake metrics, mock account names, and unsupported capability claims are prohibited from the public website.
