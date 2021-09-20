import boto3

client = boto3.client('rds')

response = client.create_db_parameter_group(
    DBParameterGroupFamily='mysql8.0',
    DBParameterGroupName='MySQLParameterGroup',
    Description='For RDS Instances running 8.0',
)
print(response)