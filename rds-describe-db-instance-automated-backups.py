import boto3

client = boto3.client('rds')
response = client.describe_db_instance_automated_backups(
    DbiResourceId='db-WXNUQNZSZJDHOQHGQ4TY6Y7IZY',
    DBInstanceIdentifier='database-instance-01'
)
print(response)