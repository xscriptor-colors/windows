<div align="center">

# Lahabana — Windows 11

Full **Windhawk + YASB** customization using the [Lahabana](https://github.com/xscriptor/xassets/blob/main/colors/colors.md) palette.

| | |
|---|---|
| **Background** | `#19191a` |
| **Text** | `#f7f1ff` |
| **Accent** | `#5ad4e6` |
| **Accent 2** | `#fc618d` |

</div>

## Structure

```
lahabana/
├── windhawk/                 # Windhawk mods (importable JSON)
│   ├── taskbar-styler.json
│   ├── start-menu-styler.json
│   ├── notification-center-styler.json
│   ├── file-explorer-styler.json
│   ├── settings-styler.json
│   ├── window-border-customizer.json
│   ├── custom-corner-radius.json
│   ├── win11-custom-title-bar-colours.json
│   ├── auto-custom-titlebar-colors.json
│   ├── dark-menus.json
│   └── setup.md              # Step-by-step installation guide
└── yasb/
    ├── config.yaml           # Bar layout and widgets
    └── styles.css            # Full theming (CSS)
```

## Windhawk

Styles the system (taskbar, start menu, notification center, file explorer,
settings, borders, corners and menus) with the Lahabana palette.

→ [View the installation guide](../../../windhawk/README.md)

## YASB

Configurable status bar with widgets for: active window, window controls,
clock/calendar, network traffic, CPU, memory, disk, volume, battery, WiFi,
weather, theme switcher and system tray.

The bar is built as **floating neumorphic islands**: the left/center/right
groups are separate pill-shaped surfaces that float over the blurred wallpaper,
with hairline highlights, soft inner shadows and pressed states. The Lahabana palette
is used with restraint — a single accent for interaction, a second accent
for power, and the remaining colors only as subtle icon tints / status states.

**Installation**
```powershell
winget install AmN.yasb
```

**Configuration** — copy `config.yaml` and `styles.css` to
`C:\Users\{user}\.config\yasb\` (or the path from the `YASB_CONFIG_HOME` env var).
Restart YASB from its tray icon.

> Requires a **Nerd Font** with the *Propo* variant so icons aren't clipped. Use
> the `NFP` family (e.g. `JetBrainsMono NFP`, v3 naming) **first** — the `NL` /
> Mono variants report a mono advance width for icon glyphs, which makes Qt size
> each icon label too narrow and clip the glyph in half. Check your installed
> name with `Get-ItemProperty` if icons still render clipped.

**Quick customization** — the palette lives in the CSS variables of `styles.css`
(`:root`): change any token and the whole bar updates.

**Theme switching** — the bar includes a `theme_switcher` button (left click:
next theme, right click: previous). It swaps `styles.css` from the
[`theme-switcher/`](../theme-switcher/) collection and YASB's `watch_stylesheet`
applies it on the spot, no restart needed.

## Palette mapping

| Token | Color | Usage |
|-------|-------|-------|
| `color0` / `background` | `#19191a` / `#19191a` | Bar background, surfaces |
| `color8` | `#19191a` | Elevated surfaces, menus |
| `color7` / `foreground` | `#f7f1ff` | Text, icons |
| `color6` | `#5ad4e6` | Primary accent, active, hover |
| `color1` | `#fc618d` | Close window, power, warnings |
| `color2` | `#7bd88f` | Battery, success |
| `color3` | `#e5ff9d` | Weather, alerts |
| `color4` | `#fd9353` | Disk, high load |
| `color5` | `#948ae3` | Media, network, GPU |
