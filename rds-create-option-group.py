import boto3

client = boto3.client('rds')
response = client.create_option_group(
    EngineName='MySQL',
    MajorEngineVersion='8.0',
    OptionGroupDescription='My MySQL 8.0 option group',
    OptionGroupName='mysql-group01',
)
print(response)