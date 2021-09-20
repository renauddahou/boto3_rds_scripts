import boto3

client = boto3.client('rds')
response = client.describe_db_log_files(
    DBInstanceIdentifier='database-instance-01',
    MaxRecords=100
)
print(response)