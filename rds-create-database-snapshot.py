import boto3

client = boto3.client('rds')
response = client.create_db_snapshot(
    DBInstanceIdentifier='database-instance-01',
    DBSnapshotIdentifier='snapshot003',
)
print(response)