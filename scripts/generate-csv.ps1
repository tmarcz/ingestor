Write-Host "Install module randomly generating names"

$size = $args[0]
Write-Host "Size file declared: $size"

if ($size -lt 1)
{
    $size = 100
    Write-Host "Size empty - using default size value: $size"
}

if (-not(Get-Module -ListAvailable -Name NameIT)) {
    Install-Module NameIT -Scope CurrentUser
}

$structure = @"
    id      = [guid]
    name    = [person]
    address = [address]
    score   = [numeric]
"@

ig $structure -AsPSObject -Count $size |  Export-Csv -Path ..\data\source\example-source.csv -NoTypeInformation

Write-Host "Done"
