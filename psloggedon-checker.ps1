<#
.SYNOPSIS
This is a simple Powershell script that runs PSLoggedOn against a host list

.DESCRIPTION
This is a simple Powershell script that runs PSLoggedOn against a list of target hosts and saves the output to a separate file

.EXAMPLE
./psloggedon-checker.ps1 -inFile target-list.txt -outFile results.txt

.NOTES
Needs to run from the same directory as PSLoggedon
#>


param (
    [string]$inFile = $(throw "-inFile is required."),
    [string]$outFile = $(throw "-outFile is required.")
)

$PSLoggedOnExist = Test-Path -Path ".\PsLoggedon.exe"

IF ($PSLoggedOnExist -eq $False){
    Write-Error "[-] This script needs to run from the same directory as PSLoggedOn.exe" -ErrorAction Stop
}

ELSE {
    foreach($line in Get-Content -Path $inFile){
        Write-Output "[*] Running PSLoggedOn.exe against $line" 
        & ".\PSLoggedOn.exe" "\\$line" | Out-File $outFile -Append
    }
    Write-Output "`n[+] Saved File $outFile"
    Write-Output "[+] Done!"
}
