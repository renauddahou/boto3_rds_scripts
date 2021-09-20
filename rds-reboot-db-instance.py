import boto3

client = boto3.client('rds')

response = client.reboot_db_instance(
    DBInstanceIdentifier='database-instance-01'
)
print(response)