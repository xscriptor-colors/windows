<#
    install.ps1 — remote bootstrap for the xscriptor-colors YASB theme pack.

    Downloads the latest snapshot of the repo from GitHub and runs the YASB
    deploy (deploy.ps1), so any Windows 11 machine can install/update the
    YASB theme pack remotely without git or manual copying.

    Remote one-liner (PowerShell 5.1+):
        irm https://raw.githubusercontent.com/xscriptor-colors/windows/main/yasb/install.ps1 | iex

    Or from a saved file:
        powershell -ExecutionPolicy Bypass -File install.ps1

    Options:
        -SkipApps   skip installing YASB via winget when missing
        -Keep       keep the downloaded snapshot (default: cleanup)
#>
param(
    [switch]$SkipApps,
    [switch]$Keep
)

$ErrorActionPreference = "Stop"
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$Repo    = "xscriptor-colors/windows"
$Branch  = "main"
$WorkDir = Join-Path $env:LOCALAPPDATA "Temp\xscriptor-colors-yasb"

Write-Host "==> Fetching $Repo@$Branch"

New-Item -ItemType Directory -Path $WorkDir -Force | Out-Null
$Zip = Join-Path $WorkDir "windows.zip"
Invoke-WebRequest -Uri "https://codeload.github.com/$Repo/zip/refs/heads/$Branch" -OutFile $Zip

Remove-Item (Join-Path $WorkDir "src") -Recurse -Force -ErrorAction SilentlyContinue
Expand-Archive -Path $Zip -DestinationPath (Join-Path $WorkDir "src") -Force

# Locate the folder that holds the YASB deploy script.
$Root = Get-ChildItem (Join-Path $WorkDir "src") -Recurse -Directory | Where-Object {
    Test-Path (Join-Path $_.FullName "yasb\deploy.ps1")
} | Select-Object -First 1

if (-not $Root) {
    throw "YASB deploy script not found in the downloaded snapshot."
}
$Src = Join-Path $Root.FullName "yasb"

if (-not $SkipApps) {
    if (-not (Get-Command yasbc -ErrorAction SilentlyContinue)) {
        Write-Host "==> Installing YASB..."
        winget install --id AmN.yasb --accept-source-agreements --accept-package-agreements
    }
}

Write-Host "==> Deploying YASB theme pack..."
& (Join-Path $Src "deploy.ps1")

if (-not $Keep) {
    Remove-Item $WorkDir -Recurse -Force
}

Write-Host ""
Write-Host "Done. Reload YASB with: yasbc reload"
