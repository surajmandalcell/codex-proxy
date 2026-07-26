# Interface design system

## Scope

The desktop renderer, product website, and generated documentation use one visual contract. The implementation is inspired by IBM Plex, IBM's public 2x Grid guidance, and Carbon's spacing and interaction principles. Subscription Proxy Inator is not affiliated with or endorsed by IBM.

## Typography

- IBM Plex Sans is the interface typeface at weights 300, 400, 500, and 600.
- IBM Plex Mono is used for routes, identifiers, logs, configuration JSON, and shell commands.
- The desktop renderer imports pinned local Fontsource packages. The website generator copies the same pinned font files into the static site.
- Primary interface text does not shrink to fit smaller windows. Layout changes before typography becomes unreadable.

## Spacing and grid

The base unit is 8 px. Layout and component spacing use multiples of that unit:

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

## Geometry

- Primary controls are at least 40 px high.
- Table rows and navigation targets are at least 40 px high; high-density data rows remain readable and keyboard reachable.
- Panels, fields, tables, and navigation use square or minimally rounded geometry.
- Borders and layer changes establish hierarchy. Gradients, glass surfaces, ambient glows, and decorative shadows are not part of the system.
- Color is functional: blue for primary action/selection, green for success, yellow for warning, and red for destructive/error states.

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

## Website structure

The website contains only project facts and direct actions. It does not display fabricated traffic, cost, latency, availability, user, or account data. Its sections are:

1. Version, license, platforms, and direct project description.
2. Implemented capabilities.
3. Provider adapter matrix.
4. Routing strategies and failure boundaries.
5. Exact local HTTP routes.
6. Security boundaries.
7. Build and project links.

## Accessibility and motion

- All interactive controls have visible focus states.
- Color is not the only status indicator; status text is always present.
- Form inputs retain visible labels.
- Reduced-motion mode disables nonessential transitions.
- Horizontal scrolling is allowed for dense tables instead of compressing columns below usable widths.
- Mobile navigation remains keyboard accessible and maintains `aria-expanded` state.

## Maintenance rules

A visual change must update tests when it changes a design contract. New components must use existing spacing, type, color, and responsive tokens before introducing new values. Marketing copy, fake metrics, mock account names, and unsupported capability claims are prohibited from the public website.
