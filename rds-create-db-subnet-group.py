import boto3

client = boto3.client('rds')

response = client.create_db_subnet_group(
    DBSubnetGroupDescription='MySQL Databases Subnet Group',
    DBSubnetGroupName='mysqldbsubnetgroup',
    SubnetIds=[
        'subnet-e44a10a8',
        'subnet-6710950c',
    ],
)
print(response)