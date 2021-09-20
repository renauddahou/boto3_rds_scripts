import boto3

client = boto3.client('rds')

response = client.create_db_instance_read_replica(
    AvailabilityZone='us-east-2c',
    CopyTagsToSnapshot=True,
    DBInstanceClass='db.t2.micro',
    DBInstanceIdentifier='db-instance-01-readreplica',
    PubliclyAccessible=True,
    SourceDBInstanceIdentifier='database-instance-01',
    StorageType='gp2',
    Tags=[
        {
            'Key': 'ReadreplicaNumber',
            'Value': 'readreplica001',
        },
    ],
)
print(response)