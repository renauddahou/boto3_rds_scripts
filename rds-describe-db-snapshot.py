import boto3

client = boto3.client('rds')
response = client.describe_db_snapshots(
    DBInstanceIdentifier='database-instance-01',
    DBSnapshotIdentifier='snapshot003',
    IncludePublic=False,
    IncludeShared=True,
    SnapshotType='manual',
)
print(response)