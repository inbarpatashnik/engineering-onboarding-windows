[CmdletBinding()] param()
. (Join-Path $PSScriptRoot '..\scripts\common.ps1'); Assert-Command docker; Import-TrainingEnv
$args=Get-ComposeArgs 6
$deadline=(Get-Date).AddMinutes(2)
do {
  & docker compose @args exec -T kafka /opt/kafka/bin/kafka-broker-api-versions.sh --bootstrap-server localhost:29092 *> $null
  if($LASTEXITCODE -eq 0){break}
  Start-Sleep -Seconds 3
} while((Get-Date)-lt$deadline)
if($LASTEXITCODE -ne 0){throw 'Kafka was not ready within two minutes. Run diagnose.ps1; do not change broker configuration.'}
& docker compose @args exec -T kafka /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:29092 --create --if-not-exists --topic ownership-events --partitions 3 --replication-factor 1
if($LASTEXITCODE -ne 0){throw 'Kafka is reachable but the training topic could not be created.'}
& docker compose @args exec -T kafka /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:29092 --describe --topic ownership-events
Write-Host 'PASS: Kafka is ready at localhost:19092. Continue with client behavior; do not tune the broker.' -ForegroundColor Green
