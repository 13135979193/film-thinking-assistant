# Windows PowerShell 5.1+: run from PowerShell or ask Codex to run this file.
param([string]$SkillsRoot = '')
$ErrorActionPreference = 'Stop'
if (-not $SkillsRoot) {
    $codexRoot = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
    $SkillsRoot = Join-Path $codexRoot 'skills'
}
$temporary = Join-Path ([IO.Path]::GetTempPath()) ('narrated-drama-' + [Guid]::NewGuid().ToString('N'))
$stage = $null
try {
    New-Item -ItemType Directory -Path $temporary -Force | Out-Null
    New-Item -ItemType Directory -Path $SkillsRoot -Force | Out-Null
    $zip = Join-Path $temporary 'repository.zip'
    Invoke-WebRequest -UseBasicParsing -Uri 'https://codeload.github.com/13135979193/film-thinking-assistant/zip/refs/heads/main' -OutFile $zip
    Expand-Archive -LiteralPath $zip -DestinationPath $temporary
    $source = Join-Path $temporary 'film-thinking-assistant-main/skills/narrated-drama-automation'
    if (-not (Test-Path (Join-Path $source 'SKILL.md'))) { throw 'Skill entrypoint missing' }
    $stage = Join-Path $SkillsRoot ('.narrated-drama-install-' + [Guid]::NewGuid().ToString('N'))
    Copy-Item -LiteralPath $source -Destination $stage -Recurse
    $target = Join-Path $SkillsRoot 'narrated-drama-automation'
    if (Test-Path $target) {
        $backupRoot = $SkillsRoot.TrimEnd([char[]]'\/') + '.backups'
        New-Item -ItemType Directory -Path $backupRoot -Force | Out-Null
        $backup = Join-Path $backupRoot ('narrated-drama-automation.' + (Get-Date -Format 'yyyyMMdd-HHmmss') + '.' + [Guid]::NewGuid().ToString('N'))
        Move-Item -LiteralPath $target -Destination $backup
        Write-Host "Previous version backed up: $backup"
    }
    Move-Item -LiteralPath $stage -Destination $target
    $stage = $null
    Write-Host "Installed: $target"
    Write-Host 'Start a new Codex turn and invoke $narrated-drama-automation with your script.'
} finally {
    if (Test-Path $temporary) { Remove-Item -LiteralPath $temporary -Recurse -Force }
    if ($stage -and (Test-Path $stage)) { Remove-Item -LiteralPath $stage -Recurse -Force }
}
