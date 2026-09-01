[CmdletBinding(SupportsShouldProcess)] param([Parameter(Mandatory)][ValidateRange(1,13)][int]$Week)
. (Join-Path $PSScriptRoot 'common.ps1')
if($PSCmdlet.ShouldProcess("week $Week training containers and volumes",'Reset')){
  & (Join-Path $PSScriptRoot 'stop-week.ps1') -Week $Week -RemoveVolumes
  & (Join-Path $PSScriptRoot 'start-week.ps1') -Week $Week
  & (Join-Path $PSScriptRoot 'smoke-test.ps1') -Week $Week
}
