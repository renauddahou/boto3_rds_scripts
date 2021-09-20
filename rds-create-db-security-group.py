import boto3

client = boto3.client('rds')

response = client.create_db_security_group(
    DBSecurityGroupDescription='MySQL DB security group',
    DBSecurityGroupName='mysqldbsecuritygroup',
)
print(response)