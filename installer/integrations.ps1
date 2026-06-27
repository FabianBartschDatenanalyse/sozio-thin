param(
    [Parameter(Mandatory = $true)]
    [string]$InstallDir,
    [switch]$Codex,
    [switch]$ClaudeCode,
    [switch]$ClaudeDesktop,
    [switch]$Uninstall,
    [string]$UserHome = $HOME,
    [string]$AppDataRoot = $env:APPDATA
)

$ErrorActionPreference = "Stop"
$exePath = Join-Path $InstallDir "sozio-thin.exe"
$logPath = Join-Path $InstallDir "integration-status.txt"
$messages = [System.Collections.Generic.List[string]]::new()
if (Test-Path -LiteralPath $logPath) {
    foreach ($line in Get-Content -LiteralPath $logPath) {
        $messages.Add($line)
    }
}

function Add-Message {
    param([string]$Message)
    $messages.Add("$(Get-Date -Format s) $Message")
}

function Write-Utf8NoBom {
    param([string]$Path, [string]$Content)
    $parent = Split-Path -Parent $Path
    if ($parent -and -not (Test-Path -LiteralPath $parent)) {
        New-Item -ItemType Directory -Path $parent -Force | Out-Null
    }
    [IO.File]::WriteAllText($Path, $Content, [Text.UTF8Encoding]::new($false))
}

function Remove-TomlSection {
    param([string]$Content, [string]$Section)
    $escaped = [regex]::Escape($Section)
    $pattern = "(?ms)^\[$escaped\]\r?\n.*?(?=^\[|\z)"
    return ([regex]::Replace($Content, $pattern, "")).TrimEnd()
}

function Configure-Codex {
    $configPath = Join-Path $UserHome ".codex\config.toml"
    $content = if (Test-Path -LiteralPath $configPath) {
        [IO.File]::ReadAllText($configPath)
    } else {
        ""
    }
    $content = Remove-TomlSection -Content $content -Section "mcp_servers.sozio-thin"
    if (-not $Uninstall) {
        $escapedExe = $exePath.Replace("\", "\\").Replace('"', '\"')
        $section = @"
[mcp_servers.sozio-thin]
command = "$escapedExe"
args = ["mcp-server"]
startup_timeout_sec = 30
tool_timeout_sec = 300
"@
        $content = ($content.TrimEnd() + "`r`n`r`n" + $section.Trim() + "`r`n").TrimStart()
        Add-Message "Codex configured in $configPath"
    } else {
        Add-Message "Codex configuration removed from $configPath"
    }
    Write-Utf8NoBom -Path $configPath -Content $content
}

function Configure-ClaudeCode {
    $claude = Get-Command claude -ErrorAction SilentlyContinue
    if (-not $claude) {
        Add-Message "Claude Code not found. Manual command is documented in Quick Start."
        return
    }
    if ($Uninstall) {
        & $claude.Source mcp remove --scope user sozio-thin 2>$null
        Add-Message "Claude Code MCP configuration removed."
        return
    }
    & $claude.Source mcp remove --scope user sozio-thin 2>$null
    & $claude.Source mcp add --scope user --transport stdio sozio-thin -- $exePath mcp-server
    if ($LASTEXITCODE -eq 0) {
        Add-Message "Claude Code configured for the current user."
    } else {
        Add-Message "Claude Code command returned exit code $LASTEXITCODE. See Quick Start."
    }
}

function Configure-ClaudeDesktop {
    $configPath = Join-Path $AppDataRoot "Claude\claude_desktop_config.json"
    $payload = [ordered]@{}
    if (Test-Path -LiteralPath $configPath) {
        try {
            $existing = [IO.File]::ReadAllText($configPath) | ConvertFrom-Json
            foreach ($property in $existing.PSObject.Properties) {
                $payload[$property.Name] = $property.Value
            }
        } catch {
            $backup = "$configPath.invalid-$(Get-Date -Format yyyyMMddHHmmss).bak"
            Copy-Item -LiteralPath $configPath -Destination $backup
            Add-Message "Claude Desktop config is invalid JSON. Backup created at $backup; no change made."
            return
        }
    }
    $servers = [ordered]@{}
    if ($payload.Contains("mcpServers") -and $payload["mcpServers"]) {
        foreach ($property in $payload["mcpServers"].PSObject.Properties) {
            if ($property.Name -ne "sozio-thin") {
                $servers[$property.Name] = $property.Value
            }
        }
    }
    if (-not $Uninstall) {
        $servers["sozio-thin"] = [ordered]@{
            command = $exePath
            args = @("mcp-server")
        }
        Add-Message "Claude Desktop configured in $configPath. Restart Claude Desktop."
    } else {
        Add-Message "Claude Desktop configuration removed from $configPath"
    }
    $payload["mcpServers"] = $servers
    Write-Utf8NoBom -Path $configPath -Content ($payload | ConvertTo-Json -Depth 30)
}

try {
    if ($Codex) {
        Configure-Codex
    }
    if ($ClaudeCode) {
        Configure-ClaudeCode
    }
    if ($ClaudeDesktop) {
        Configure-ClaudeDesktop
    }
} catch {
    Add-Message "ERROR: $($_.Exception.Message)"
}

if (Test-Path -LiteralPath $InstallDir) {
    Write-Utf8NoBom -Path $logPath -Content (($messages -join "`r`n") + "`r`n")
}
