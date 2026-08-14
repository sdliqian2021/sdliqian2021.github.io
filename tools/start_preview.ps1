$ErrorActionPreference = "Stop"
$repository = Split-Path -Parent $PSScriptRoot
$preview = Join-Path $PSScriptRoot "preview_sites.py"
$python = Get-Command python -ErrorAction Stop

Push-Location $repository
try {
    & $python.Source $preview @args
}
finally {
    Pop-Location
}
