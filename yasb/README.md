# YASB — xscriptor-colors theme pack

12 themes for **YASB** (Yet Another Status Bar) sharing one config and a theme
switcher button. Every stylesheet keeps the same floating-island look; only the
palette changes.

| Theme | Background | Text | Accent | Accent 2 |
|---|---|---|---|---|
| X | `#050505` | `#f7f1ff` | `#5ad4e6` | `#fc618d` |
| Madrid | `#fafafa` | `#1a1a1a` | `#007a9e` | `#990026` |
| Lahabana | `#19191a` | `#f7f1ff` | `#5ad4e6` | `#fc618d` |
| Miami | `#000000` | `#f7f1ff` | `#47cfff` | `#ff4c8b` |
| Paris | `#1a0a30` | `#f7f1ff` | `#a3f3ff` | `#fc618d` |
| Tokio | `#1c1c1d` | `#f7f1ff` | `#5ad4e6` | `#fc618d` |
| Oslo | `#3f4451` | `#abb2bf` | `#42b3c2` | `#e05561` |
| Helsinki | `#f8fafe` | `#544d40` | `#bd4c3d` | `#1faa9e` |
| Berlin | `#000000` | `#cccccc` | `#cccccc` | `#999999` |
| London | `#ffffff` | `#333333` | `#888888` | `#333333` |
| Praha | `#1a1a1a` | `#ffffff` | `#8be9fd` | `#ff5555` |
| Bogota | `#200b0a` | `#f7f1ff` | `#47e6ff` | `#fc618d` |

> Source palettes: [`xassets/colors/colors.md`](https://github.com/xscriptor/xassets/blob/main/colors/colors.md)

## Structure

```
yasb/
├── config.yaml            # single config for every theme (includes theme_switcher)
├── themes/
│   ├── styles.x.css       # base theme — source of truth for the look
│   └── styles.<theme>.css # 12 stylesheets, one per theme
├── theme-switcher.ps1     # switcher logic (next / prev / name)
├── deploy.ps1             # installs everything into the YASB config dir
├── generate.py            # regenerates the 12 stylesheets from the X base
└── README.md
```

## Install

Requires [YASB](https://github.com/amnweb/yasb) (`winget install AmN.yasb`) and a
**Nerd Font** with the *Propo* variant (e.g. `JetBrainsMono NFP`).

**Remote** (no git needed — installs YASB if missing, then deploys):

```powershell
irm https://raw.githubusercontent.com/xscriptor-colors/windows/main/yasb/install.ps1 | iex
```

**Or locally from this folder:**

```powershell
powershell -ExecutionPolicy Bypass -File deploy.ps1
yasbc reload
```

`deploy.ps1` copies `config.yaml`, the 12 `styles.*.css` and the switcher script
into the YASB config dir (`%USERPROFILE%\.config\yasb`, or `$env:YASB_CONFIG_HOME`
when set), points the switcher at the real location, backs up your previous
`config.yaml` / `styles.css` as `*.bak` and keeps your active theme.

## Theme switcher

The bar has a `theme_switcher` button (paint-brush glyph) at the right, before
the power button — its label shows the current theme.

- **Left click**: next theme · **Right click**: previous theme
- Switching only overwrites `styles.css`; YASB's `watch_stylesheet` applies it
  on the spot, no restart needed.

The power button (Windows-logo glyph) opens the power menu.

## Customization

- **Palette**: edit the `--x-*` CSS variables in `themes/styles.x.css` (or any
  `styles.<theme>.css`), then re-run `deploy.ps1`.
- **New theme**: add its palette to `PALETTES` in `generate.py`, run
  `python generate.py`, then `deploy.ps1`. The derived colors (islands, dim
  text, gradients, shadows, glows) are recomputed automatically.
- **Layout / widgets**: edit `config.yaml`, then re-run `deploy.ps1`.

> If your config dir path contains spaces, the switcher *label* may stay on the
> icon placeholder (YASB splits `run_cmd` on spaces and cannot be quoted); the
> switcher clicks still work.
