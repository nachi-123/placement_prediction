$ErrorActionPreference = 'Stop'

$source = Get-Location
$target = Join-Path $env:TEMP 'placement_prediction_build'

if (Test-Path $target) {
    Remove-Item -Recurse -Force $target
}

New-Item -ItemType Directory -Path $target | Out-Null

# Mirror the repo into a non-OneDrive temp path to avoid Docker context issues on reparse-point files.
robocopy $source $target /MIR /XD pp .git __pycache__ catboost_info logs notebook artifacts | Out-Null

if ($LASTEXITCODE -ge 8) {
    throw "robocopy failed with exit code $LASTEXITCODE"
}

docker build -t placement-app $target
