import boto3

client = boto3.client('rds')
response = client.delete_db_instance(
    DBInstanceIdentifier='db-instance-01-readreplica',
    SkipFinalSnapshot=True,
)
print(response)