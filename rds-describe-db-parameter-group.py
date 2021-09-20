import boto3

client = boto3.client('rds')
response = client.describe_db_parameters(
    DBParameterGroupName='mysqlparametergroup',
    MaxRecords=30
)
print(response)