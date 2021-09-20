import boto3

client = boto3.client('rds')
response = client.delete_db_snapshot(
    DBSnapshotIdentifier='snapshot003',
)
print(response)