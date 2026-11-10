# Zebar — xscriptor-colors packs

Status bar packs for [Zebar](https://github.com/glzr-io/zebar). Each subfolder
is a self-contained pack (has its own `zpack.json`), mirroring what lives in
`~/.glzr/zebar/`.

## Packs

| Folder | Pack id | Design |
|---|---|---|
| `neumorphism/` | `xscriptor-colors-neumorphism` | One neumorphic island-widget per indicator (dock at top center) + calendar popup, 12 switchable palettes |
| `xneon/` | `xneon` | Liquid-glass islands — saved copy of an earlier design |

`neumorphism/` widgets: `system` (host · IP · keyboard layout), `media`
(click = play/pause), `disk`, `clock` (click = calendar popup; Esc/click
again to close), `cpu`, `memory`, `traffic` (down/up), `volume` (click =
mute), `battery` and `theme` (click = cycle the 12 palettes across every
widget). The old single-bar layout is kept as the `bar` widget (not started
by default).

## Install Zebar

```powershell
winget install glzr-io.zebar
```

Requires [WebView2](https://developer.microsoft.com/en-us/microsoft-edge/webview2/)
(usually preinstalled on Windows 11) and the Hack Nerd Font (or any Nerd Font).

## Deploy

**Remote** (no git needed — installs Zebar if missing, then deploys):

```powershell
irm https://raw.githubusercontent.com/xscriptor-colors/windows/main/zebar/install.ps1 | iex
```

**Or locally from this folder:**

```powershell
powershell -ExecutionPolicy Bypass -File deploy.ps1
```

Copies every pack into `~/.glzr/zebar/` (same folder names, backups as
`<name>.bak`). Then run it from the Zebar tray icon → *My widgets*.

## Customization

- **Palette**: the widgets' CSS variables are themeable at runtime
  (`palettes.js`). Regenerate it after adding a palette to the canonical
  `yasb/generate.py` PALETTES:

  ```powershell
  python generate-palettes.py
  ```

- **Look & layout**: edit `neumorphism/styles.css` (shared neumorphic island
  style) and the per-widget `*.html` files. Dock positions live in
  `neumorphism/zpack.json` presets (`offsetX`), computed as a centered row.
  The neumorphic recipe: dual soft shadows (light top-left / dark
  bottom-right), same-surface colors, inset bevels for the recessed islands.

- Widgets share state through `localStorage` (`core.js`): the `theme` widget
  cycles palettes and every widget follows; the `clock` widget toggles the
  calendar via the `xscriptor-calendar` key and `zebar.startWidget()`.

- Widget files are kept flat at each pack root (like the starter pack): Zebar's
  asset server only serves files matching the `includeFiles` globs, and Rust
  globs do not cross path separators.
