import boto3

client = boto3.client('rds')
response = client.create_event_subscription(
    Enabled=True,
    EventCategories=[
        'availability',
    ],
    SnsTopicArn='arn:aws:sns:us-east-2:585584209241:mysql',
    SourceIds=[
        'database-instance-01',
    ],
    SourceType='db-instance',
    SubscriptionName='mysqleventsubscription',
)
print(response)