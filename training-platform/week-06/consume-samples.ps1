[CmdletBinding()] param([string]$Group='student-week06',[ValidateRange(1,100)][int]$MaxMessages=6)
. (Join-Path $PSScriptRoot '..\scripts\common.ps1'); Assert-Command docker; Import-TrainingEnv
$args=Get-ComposeArgs 6
& docker compose @args exec -T kafka /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:29092 --topic ownership-events --group $Group --from-beginning --max-messages $MaxMessages --property print.key=true --property print.partition=true --property print.offset=true
if($LASTEXITCODE -ne 0){throw 'Sample consumption failed or fewer records were available than requested.'}
