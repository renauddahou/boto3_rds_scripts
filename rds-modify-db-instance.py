import boto3

client = boto3.client('rds')

response = client.modify_db_instance(
    DBInstanceIdentifier='database-instance-01',
    MasterUserPassword='new-pa$$word'
  )  
print(response)