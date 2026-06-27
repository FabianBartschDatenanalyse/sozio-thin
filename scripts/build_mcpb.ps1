param(
    [Parameter(Mandatory = $true)]
    [string]$BinaryRoot
)

$ErrorActionPreference = "Stop"
$root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$resolvedBinaryRoot = (Resolve-Path -LiteralPath $BinaryRoot).Path
$tempRoot = [IO.Path]::GetFullPath((Join-Path $env:TEMP "sozio-thin-mcpb-build"))
$bundleRoot = Join-Path $tempRoot "bundle"
$serverRoot = Join-Path $bundleRoot "server"
$release = Join-Path $root "release"
$manifestSource = Join-Path $root "mcpb\manifest.json"
$output = Join-Path $release "Sozio-Thin-0.1.2-Windows-x64.mcpb"

if (-not (Test-Path -LiteralPath (Join-Path $resolvedBinaryRoot "sozio-thin.exe"))) {
    throw "Standalone executable not found below BinaryRoot: $resolvedBinaryRoot"
}

foreach ($target in @($tempRoot, $output)) {
    $full = [IO.Path]::GetFullPath($target)
    $insideRelease = $full.StartsWith($release, [StringComparison]::OrdinalIgnoreCase)
    $insideDedicatedTemp = $full.StartsWith($tempRoot, [StringComparison]::OrdinalIgnoreCase)
    if (-not ($insideRelease -or $insideDedicatedTemp)) {
        throw "Unsafe MCPB build path: $full"
    }
    if (Test-Path -LiteralPath $full) {
        Remove-Item -LiteralPath $full -Recurse -Force
    }
}

New-Item -ItemType Directory -Path $serverRoot -Force | Out-Null
New-Item -ItemType Directory -Path $release -Force | Out-Null
Copy-Item -LiteralPath $manifestSource -Destination (Join-Path $bundleRoot "manifest.json")
Copy-Item -LiteralPath (Join-Path $root "README.md") -Destination $bundleRoot
Copy-Item -LiteralPath (Join-Path $root "LICENSE") -Destination $bundleRoot
Copy-Item -Path (Join-Path $resolvedBinaryRoot "*") -Destination $serverRoot -Recurse -Force

& npx -y "@anthropic-ai/mcpb@2.1.2" validate (Join-Path $bundleRoot "manifest.json")
if ($LASTEXITCODE -ne 0) {
    throw "MCPB manifest validation failed with exit code $LASTEXITCODE"
}

& npx -y "@anthropic-ai/mcpb@2.1.2" pack $bundleRoot $output
if ($LASTEXITCODE -ne 0) {
    throw "MCPB packing failed with exit code $LASTEXITCODE"
}

& npx -y "@anthropic-ai/mcpb@2.1.2" info $output
if ($LASTEXITCODE -ne 0) {
    throw "MCPB inspection failed with exit code $LASTEXITCODE"
}

Get-Item -LiteralPath $output | Select-Object Name, Length, FullName
