import boto3

client = boto3.client('rds')
response = client.promote_read_replica(
    BackupRetentionPeriod=5,
    DBInstanceIdentifier='db-instance-01-readreplica',
)
print(response)