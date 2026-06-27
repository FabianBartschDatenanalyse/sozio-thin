param(
    [string]$IsccPath
)

$ErrorActionPreference = "Stop"
$root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$tempRoot = [IO.Path]::GetFullPath((Join-Path $env:TEMP "sozio-thin-installer-build"))
$build = Join-Path $tempRoot "build"
$dist = Join-Path $tempRoot "dist"
$release = Join-Path $root "release"

if (-not $IsccPath) {
    $isccCandidates = @(
        (Join-Path $env:LOCALAPPDATA "Programs\Inno Setup 6\ISCC.exe"),
        "C:\Program Files (x86)\Inno Setup 6\ISCC.exe",
        "C:\Program Files\Inno Setup 6\ISCC.exe"
    )
    $IsccPath = $isccCandidates | Where-Object { Test-Path -LiteralPath $_ } | Select-Object -First 1
}

foreach ($target in @($tempRoot, $release, (Join-Path $root "build"), (Join-Path $root "dist"))) {
    $full = [IO.Path]::GetFullPath($target)
    $insideProduct = $full.StartsWith($root, [StringComparison]::OrdinalIgnoreCase)
    $insideDedicatedTemp = $full.StartsWith($tempRoot, [StringComparison]::OrdinalIgnoreCase)
    if (-not ($insideProduct -or $insideDedicatedTemp)) {
        throw "Unsafe build path: $full"
    }
    if (Test-Path -LiteralPath $full) {
        Remove-Item -LiteralPath $full -Recurse -Force
    }
}

Push-Location $root
try {
    & uv run --with pyinstaller pyinstaller `
        --noconfirm `
        --clean `
        --onedir `
        --contents-directory . `
        --name sozio-thin `
        --console `
        --collect-submodules mcp.server `
        --collect-all duckdb `
        --collect-all sqlglot `
        --add-data "$root\catalog;catalog" `
        --distpath $dist `
        --workpath $build `
        --specpath $build `
        "$root\src\sozio_thin\__main__.py"
    if ($LASTEXITCODE -ne 0) {
        throw "PyInstaller failed with exit code $LASTEXITCODE"
    }

    & (Join-Path $dist "sozio-thin\sozio-thin.exe") doctor
    if ($LASTEXITCODE -ne 0) {
        throw "Standalone executable failed its doctor check."
    }

    if (-not (Test-Path -LiteralPath $IsccPath)) {
        throw "Inno Setup compiler not found at $IsccPath"
    }
    $buildRoot = Join-Path $dist "sozio-thin"
    & $IsccPath "/DBuildRoot=$buildRoot" (Join-Path $root "installer\sozio-thin.iss")
    if ($LASTEXITCODE -ne 0) {
        throw "Inno Setup failed with exit code $LASTEXITCODE"
    }

    Get-ChildItem $release -File | Select-Object Name, Length, FullName
} finally {
    Pop-Location
}
