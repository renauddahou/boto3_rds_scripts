import boto3

client = boto3.client('rds')
response = client.create_db_proxy(
    DBProxyName='MySQLDBProxy',
    EngineFamily='MYSQL',
    Auth=[
        {
            'Description': 'UserLogin',
            'UserName': 'admin01',
            'SecretArn': 'arn:aws:secretsmanager:us-east-2:585584209241:secret:mysql-01-database-secret-KV9YjW'
        },
    ],
    RoleArn='arn:aws:iam::585584209241:user/test',
    VpcSubnetIds=[
        'subnet-e44a10a8',
        'subnet-6710950c'
    ],
    VpcSecurityGroupIds=[
        'sg-6dbc5f1b',
    ],
    RequireTLS=True,
    IdleClientTimeout=123,
    DebugLogging=False
)
print(response)