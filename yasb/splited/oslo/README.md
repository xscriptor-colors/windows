<div align="center">

# Oslo — Windows 11

Full **Windhawk + YASB** customization using the [Oslo](https://github.com/xscriptor/xassets/blob/main/colors/colors.md) palette.

| | |
|---|---|
| **Background** | `#3f4451` |
| **Text** | `#abb2bf` |
| **Accent** | `#42b3c2` |
| **Accent 2** | `#e05561` |

</div>

## Structure

```
oslo/
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
settings, borders, corners and menus) with the Oslo palette.

→ [View the installation guide](../../../windhawk/README.md)

## YASB

Configurable status bar with widgets for: active window, window controls,
clock/calendar, network traffic, CPU, memory, disk, volume, battery, WiFi,
weather, theme switcher and system tray.

The bar is built as **floating neumorphic islands**: the left/center/right
groups are separate pill-shaped surfaces that float over the blurred wallpaper,
with hairline highlights, soft inner shadows and pressed states. The Oslo palette
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
| `color0` / `background` | `#3f4451` / `#3f4451` | Bar background, surfaces |
| `color8` | `#4f5666` | Elevated surfaces, menus |
| `color7` / `foreground` | `#abb2bf` | Text, icons |
| `color6` | `#42b3c2` | Primary accent, active, hover |
| `color1` | `#e05561` | Close window, power, warnings |
| `color2` | `#8cc265` | Battery, success |
| `color3` | `#d18f52` | Weather, alerts |
| `color4` | `#4aa5f0` | Disk, high load |
| `color5` | `#c162de` | Media, network, GPU |
