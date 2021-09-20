import boto3

client = boto3.client('rds')

response = client.create_db_instance(
    AllocatedStorage=5,
    DBInstanceClass='db.t2.micro',
    DBInstanceIdentifier='database-instance-01',
    Engine='MySQL',
    MasterUserPassword='testpw0021',
    MasterUsername='admin01',
)

print(response)