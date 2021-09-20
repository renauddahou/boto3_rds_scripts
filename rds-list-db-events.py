import boto3

client = boto3.client('rds')
response = client.describe_events(
    Duration=10080,
    EventCategories=[
        'backup',
    ],
    SourceIdentifier='database-instance-01',
    SourceType='db-instance',
)
print(response)