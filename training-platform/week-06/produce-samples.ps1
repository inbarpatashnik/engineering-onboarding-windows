[CmdletBinding()] param()
. (Join-Path $PSScriptRoot '..\scripts\common.ps1'); Assert-Command docker; Import-TrainingEnv
$args=Get-ComposeArgs 6
$records=@(
  'resource-1:{"event_id":"evt-001","resource_id":"resource-1","owner":"team-a","version":1}',
  'resource-2:{"event_id":"evt-002","resource_id":"resource-2","owner":"team-b","version":1}',
  'resource-1:{"event_id":"evt-003","resource_id":"resource-1","owner":"team-c","version":1}',
  'resource-3:{broken-json',
  'resource-2:{"event_id":"evt-004","resource_id":"resource-2","owner":"team-d","version":99}',
  'resource-1:{"event_id":"evt-003","resource_id":"resource-1","owner":"team-c","version":1}'
) -join "`n"
$records | & docker compose @args exec -T kafka /opt/kafka/bin/kafka-console-producer.sh --bootstrap-server localhost:29092 --topic ownership-events --property parse.key=true --property key.separator=:
if($LASTEXITCODE -ne 0){throw 'Sample production failed.'}
Write-Host 'Published six samples: ordered keys, poison JSON, unknown version, and a duplicate event ID.' -ForegroundColor Green
