import boto3

client = boto3.client('rds')
response = client.describe_valid_db_instance_modifications(
    DBInstanceIdentifier='database-instance-01'
)
print(response)