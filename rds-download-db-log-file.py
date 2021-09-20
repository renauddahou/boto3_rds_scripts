import boto3

client = boto3.client('rds')
response = client.download_db_log_file_portion(
    DBInstanceIdentifier='database-instance-01',
    LogFileName='error/mysql-error-running.log',
)
print(response)