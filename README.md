<h1 align="center"> Taking <em>Windows</em> to perfection  <img src="https://raw.githubusercontent.com/xscriptor-colors/web/main/public/svg/icons/windows.svg" width="20" alt="Windows Colors logo" />
</h1>

<div align="center">
Complete collection of Xscriptor customizations for **Windows 11**: status bars
(YASB, Zebar), taskbar themes, PowerShell tooling and more — all with the
Xscriptor palette ecosystem.

[![Windows](https://img.shields.io/badge/Windows-0078D6?logo=windows&logoColor=white)](https://github.com/xscriptor-colors/windows)
[![YASB](https://img.shields.io/badge/YASB-007ACC)](https://github.com/amnweb/yasb)
[![Zebar](https://img.shields.io/badge/Zebar-4B32C3)](https://github.com/glzr-io/zebar)
[![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?logo=powershell&logoColor=white)](https://github.com/PowerShell/PowerShell)
[![CSS](https://img.shields.io/badge/CSS-1572B6?logo=css3&logoColor=fff)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=000)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![MIT](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

</div>

<div align="center">

<h2 id="contents">Contents</h2>

<nav>
  <a href="#previews">Previews</a> ·
  <a href="#repository-structure">Repository Structure</a> ·
  <a href="#quick-install">Quick Install</a> ·
  <a href="#usage">Usage</a> ·
  <a href="#colors">Colors</a> ·
  <a href="#compatibility">Compatibility</a> ·
  <a href="#license">License</a> ·
  <a href="#related-repos">Related Repos</a> ·
  <a href="#x">X</a>
</nav>

</div>



<h2 align="center" id="previews">Previews</h2>
<div align="center">
<img src="https://xscriptor-colors.github.io/web/images/windows/preview1.webp" width="900" alt="Demo" >

<hr />
<img src="https://xscriptor-colors.github.io/web/images/windows/preview2.webp" width="900" alt="Demo" >
<hr />
</div>

<details>
<summary><b>More... </b></summary>
<p align="center">
<img src="https://xscriptor-colors.github.io/web/images/windows/preview3.webp" alt="Demo" width="49%" />
<img src="https://xscriptor-colors.github.io/web/images/windows/preview4.webp" alt="Demo" width="49%" />
</p>
</details>

<div align="center">

<h2 id="repository-structure">Repository Structure</h2>

</div>

- `yasb/`: YASB theme pack — single source layout (`config.yaml`, `themes/`,
  theme switcher, `deploy.ps1`, `generate.py`) plus the archived per-theme
  folders in `yasb/splited/`.
- `zebar/`: Zebar widget packs — `neumorphism/` (soft-UI neumorphic bar with
  popups and 12 switchable palettes) and `xneon/` (liquid-glass backup),
  with `deploy.ps1` and `generate-palettes.py`.
- `windhawk/`: Windhawk taskbar themes (Taskbar Styler JSON) — three layouts:
  `dock/` (floating centered dock), `islands/` (floating rounded islands),
  `translucid/` (legacy transparent); each with one variant per palette
  (`x.json`, `madrid.json`, …) and its own accent color; `taskbar/generate.py`
  regenerates them from the canonical palettes.

<div align="center">

<h2 id="quick-install">Quick Install</h2>

</div>

**Remote one-liners** (Windows 11, PowerShell 5.1+, no git needed) — install
the app if missing and deploy the theme packs from the repo:

```powershell
irm https://raw.githubusercontent.com/xscriptor-colors/windows/main/yasb/install.ps1 | iex                         # YASB only
irm https://raw.githubusercontent.com/xscriptor-colors/windows/main/zebar/install.ps1 | iex                        # Zebar only
```

**Or clone and deploy locally**:

```powershell
powershell -ExecutionPolicy Bypass -File yasb\deploy.ps1   # YASB (winget install AmN.yasb)
powershell -ExecutionPolicy Bypass -File zebar\deploy.ps1  # Zebar (winget install glzr-io.zebar)
```

Then enable the packs from the Zebar tray icon → *My widgets*.

<div align="center">

<h2 id="usage">Usage</h2>

</div>

- **Zebar bar**: one neumorphic island per indicator (system, media, disk,
  clock, CPU, memory, traffic, volume, battery, theme). Click any island for
  its detail popup (calendar, controls, usage charts); click the paintbrush
  to cycle the 12 palettes across every widget; click volume to mute.
- **YASB bar**: floating neumorphic islands; `theme_switcher` button cycles
  the 12 theme stylesheets (left = next, right = previous).

<div align="center">

<h2 id="colors">Colors</h2>

</div>


<div align="center">
  <a href="https://raw.githubusercontent.com/xscriptor-colors/assets/main/media/palettes/palette_x.svg"><img src="https://raw.githubusercontent.com/xscriptor-colors/assets/main/media/palettes/palette_x.svg" height="100" alt="X"/></a>
  <a href="https://raw.githubusercontent.com/xscriptor-colors/assets/main/media/palettes/palette_madrid.svg"><img src="https://raw.githubusercontent.com/xscriptor-colors/assets/main/media/palettes/palette_madrid.svg" height="100" alt="Madrid"/></a>
  <a href="https://raw.githubusercontent.com/xscriptor-colors/assets/main/media/palettes/palette_lahabana.svg"><img src="https://raw.githubusercontent.com/xscriptor-colors/assets/main/media/palettes/palette_lahabana.svg" height="100" alt="Lahabana"/></a>
  <a href="https://raw.githubusercontent.com/xscriptor-colors/assets/main/media/palettes/palette_miami.svg"><img src="https://raw.githubusercontent.com/xscriptor-colors/assets/main/media/palettes/palette_miami.svg" height="100" alt="Miami"/></a>
  <a href="https://raw.githubusercontent.com/xscriptor-colors/assets/main/media/palettes/palette_paris.svg"><img src="https://raw.githubusercontent.com/xscriptor-colors/assets/main/media/palettes/palette_paris.svg" height="100" alt="Paris"/></a>
  <a href="https://raw.githubusercontent.com/xscriptor-colors/assets/main/media/palettes/palette_tokio.svg"><img src="https://raw.githubusercontent.com/xscriptor-colors/assets/main/media/palettes/palette_tokio.svg" height="100" alt="Tokio"/></a>
</div>
<div align="center">
  <a href="https://raw.githubusercontent.com/xscriptor-colors/assets/main/media/palettes/palette_oslo.svg"><img src="https://raw.githubusercontent.com/xscriptor-colors/assets/main/media/palettes/palette_oslo.svg" height="100" alt="Oslo"/></a>
  <a href="https://raw.githubusercontent.com/xscriptor-colors/assets/main/media/palettes/palette_helsinki.svg"><img src="https://raw.githubusercontent.com/xscriptor-colors/assets/main/media/palettes/palette_helsinki.svg" height="100" alt="Helsinki"/></a>
  <a href="https://raw.githubusercontent.com/xscriptor-colors/assets/main/media/palettes/palette_berlin.svg"><img src="https://raw.githubusercontent.com/xscriptor-colors/assets/main/media/palettes/palette_berlin.svg" height="100" alt="Berlin"/></a>
  <a href="https://raw.githubusercontent.com/xscriptor-colors/assets/main/media/palettes/palette_london.svg"><img src="https://raw.githubusercontent.com/xscriptor-colors/assets/main/media/palettes/palette_london.svg" height="100" alt="London"/></a>
  <a href="https://raw.githubusercontent.com/xscriptor-colors/assets/main/media/palettes/palette_praha.svg"><img src="https://raw.githubusercontent.com/xscriptor-colors/assets/main/media/palettes/palette_praha.svg" height="100" alt="Praha"/></a>
  <a href="https://raw.githubusercontent.com/xscriptor-colors/assets/main/media/palettes/palette_bogota.svg"><img src="https://raw.githubusercontent.com/xscriptor-colors/assets/main/media/palettes/palette_bogota.svg" height="100" alt="Bogota"/></a>
</div>

<div align="center">

<h2 id="compatibility">Compatibility</h2>

</div>

- Windows 11, Komorebi/GlazeWM-friendly.
- Requires the Hack Nerd Font (or any Nerd Font) for icon glyphs.

<div align="center">

<h2 id="license">License</h2>

</div>

- Repository code is under the [MIT License](LICENSE).

<div align="center">

<h2 id="related-repos">Related Repos</h2>

</div>

- [VSCode](https://github.com/xscriptor-colors/vscode)
- [Terminal](https://github.com/xscriptor-colors/terminal)
- [Nvim](https://github.com/xscriptor-colors/nvim)
- [Jetbrains](https://github.com/xscriptor-colors/jetbrains)

<div align="center">
<h2 id="x">X</h2>
<a href="https://xscriptor.io">Dev</a>
 & 
<a href="https://github.com/xscriptor">github</a>
 & 
<a href="https://www.xscriptor.com">X</a>
</div>