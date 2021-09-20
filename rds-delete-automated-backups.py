import boto3

client = boto3.client('rds')
response = client.delete_db_instance_automated_backup(
    DbiResourceId='db-WXNUQNZSZJDHOQHGQ4TY6Y7IZY',
    DBInstanceAutomatedBackupsArn='rn:aws:rds:us-east-2:585584209241:auto-backup:ab-wxnuqnzszjdhoqhgq4ty6y7izzxjg7yf7cgdchq'
)
print(response)