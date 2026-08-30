$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
$Cursor = Join-Path $Root ".cursor"
New-Item -ItemType Directory -Force -Path $Cursor | Out-Null

foreach ($Name in @("skills", "agents")) {
    $Link = Join-Path $Cursor $Name
    $Target = Join-Path $Root $Name
    if (Test-Path $Link) {
        $Item = Get-Item $Link -Force
        if ($Item.Attributes -band [IO.FileAttributes]::ReparsePoint) {
            $Item.Delete()
        } else {
            Remove-Item -Recurse -Force $Link
        }
    }
    New-Item -ItemType Junction -Path $Link -Target $Target | Out-Null
}

Write-Host "Linked .cursor/skills -> skills"
Write-Host "Linked .cursor/agents -> agents"
