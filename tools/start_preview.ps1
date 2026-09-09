$ErrorActionPreference = "Stop"
$repository = Split-Path -Parent $PSScriptRoot
$preview = Join-Path $PSScriptRoot "preview_sites.py"

function Resolve-PythonCommand {
    $python = Get-Command python -ErrorAction SilentlyContinue
    if ($python) {
        return @($python.Source)
    }
    $launcher = Get-Command py -ErrorAction SilentlyContinue
    if ($launcher) {
        return @($launcher.Source, "-3")
    }
    $installed = Join-Path $env:LOCALAPPDATA "Programs\Python"
    if (Test-Path -LiteralPath $installed -PathType Container) {
        $candidates = @()
        foreach ($directory in Get-ChildItem -LiteralPath $installed -Directory) {
            if ($directory.Name -match "^Python(\d)(\d+)$") {
                $executable = Join-Path $directory.FullName "python.exe"
                if (Test-Path -LiteralPath $executable -PathType Leaf) {
                    $candidates += [pscustomobject]@{
                        Version = [version]("{0}.{1}" -f $Matches[1], $Matches[2])
                        Executable = $executable
                    }
                }
            }
        }
        if ($candidates.Count -gt 0) {
            $newest = $candidates | Sort-Object Version -Descending | Select-Object -First 1
            return @($newest.Executable)
        }
    }
    throw "Python 3 was not found. Install it, or put python.exe or py.exe on PATH."
}

$command = Resolve-PythonCommand
$executable = $command[0]
$prefixArguments = @($command | Select-Object -Skip 1)
Write-Output "Python: $executable $prefixArguments"

Push-Location $repository
try {
    & $executable @prefixArguments $preview @args
}
finally {
    Pop-Location
}
