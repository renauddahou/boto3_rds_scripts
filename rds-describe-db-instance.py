import boto3

client = boto3.client('rds')

response = client.describe_db_instances(
    DBInstanceIdentifier='database-instance-01',
)
print(response)