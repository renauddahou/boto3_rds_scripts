import boto3

client = boto3.client('rds')

response = client.describe_db_engine_versions(
    Engine='MySQL',
    EngineVersion='8.0.23'
)
print(response)