#define MyAppName "Sozio Thin"
#define MyAppVersion "0.1.1"
#define MyAppPublisher "Fabian Bartsch"
#define MyAppURL "https://github.com/FabianBartschDatenanalyse/sozio-thin"
#ifndef BuildRoot
  #define BuildRoot "..\dist\sozio-thin"
#endif

[Setup]
AppId={{8548907D-CA71-449D-AC9E-36E875D3DBE8}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}/issues
AppUpdatesURL={#MyAppURL}/releases
DefaultDirName={localappdata}\Programs\Sozio Thin
DefaultGroupName=Sozio Thin
DisableProgramGroupPage=yes
PrivilegesRequired=lowest
OutputDir=..\release
OutputBaseFilename=Sozio-Thin-Setup-{#MyAppVersion}-Windows-x64
Compression=lzma2/ultra64
SolidCompression=yes
WizardStyle=modern
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
UninstallDisplayIcon={app}\sozio-thin.exe
LicenseFile=..\LICENSE
InfoAfterFile=..\NOTICE.md

[Languages]
Name: "german"; MessagesFile: "compiler:Languages\German.isl"
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "codex"; Description: "In Codex einrichten"; GroupDescription: "MCP-Clients:"; Flags: checkedonce
Name: "claudecode"; Description: "In Claude Code einrichten (falls installiert)"; GroupDescription: "MCP-Clients:"; Flags: checkedonce
Name: "claudedesktop"; Description: "In Claude Desktop einrichten"; GroupDescription: "MCP-Clients:"

[Files]
Source: "{#BuildRoot}\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "integrations.ps1"; DestDir: "{app}"; Flags: ignoreversion
Source: "quickstart.html"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\README.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\LICENSE"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\NOTICE.md"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Sozio Thin - Schnellstart"; Filename: "{app}\quickstart.html"
Name: "{group}\Sozio Thin - Diagnose"; Filename: "{cmd}"; Parameters: "/k ""{app}\sozio-thin.exe"" doctor"
Name: "{group}\Sozio Thin deinstallieren"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\sozio-thin.exe"; Parameters: "doctor"; StatusMsg: "Katalog wird geprüft..."; Flags: runhidden waituntilterminated
Filename: "powershell.exe"; Parameters: "-NoProfile -ExecutionPolicy Bypass -File ""{app}\integrations.ps1"" -InstallDir ""{app}"" -Codex"; StatusMsg: "Codex wird eingerichtet..."; Tasks: codex; Flags: runhidden waituntilterminated
Filename: "powershell.exe"; Parameters: "-NoProfile -ExecutionPolicy Bypass -File ""{app}\integrations.ps1"" -InstallDir ""{app}"" -ClaudeCode"; StatusMsg: "Claude Code wird eingerichtet..."; Tasks: claudecode; Flags: runhidden waituntilterminated
Filename: "powershell.exe"; Parameters: "-NoProfile -ExecutionPolicy Bypass -File ""{app}\integrations.ps1"" -InstallDir ""{app}"" -ClaudeDesktop"; StatusMsg: "Claude Desktop wird eingerichtet..."; Tasks: claudedesktop; Flags: runhidden waituntilterminated
Filename: "{app}\quickstart.html"; Description: "Schnellstart öffnen"; Flags: postinstall shellexec skipifsilent

[UninstallRun]
Filename: "powershell.exe"; Parameters: "-NoProfile -ExecutionPolicy Bypass -File ""{app}\integrations.ps1"" -InstallDir ""{app}"" -Codex -Uninstall"; Tasks: codex; Flags: runhidden waituntilterminated; RunOnceId: "RemoveCodex"
Filename: "powershell.exe"; Parameters: "-NoProfile -ExecutionPolicy Bypass -File ""{app}\integrations.ps1"" -InstallDir ""{app}"" -ClaudeCode -Uninstall"; Tasks: claudecode; Flags: runhidden waituntilterminated; RunOnceId: "RemoveClaudeCode"
Filename: "powershell.exe"; Parameters: "-NoProfile -ExecutionPolicy Bypass -File ""{app}\integrations.ps1"" -InstallDir ""{app}"" -ClaudeDesktop -Uninstall"; Tasks: claudedesktop; Flags: runhidden waituntilterminated; RunOnceId: "RemoveClaudeDesktop"
