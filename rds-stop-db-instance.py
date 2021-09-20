import boto3

client = boto3.client('rds')

response = client.stop_db_instance(
    DBInstanceIdentifier='database-instance-01',
    DBSnapshotIdentifier='stop-snapshot001'
)
print(response)