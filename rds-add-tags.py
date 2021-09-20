import boto3

client = boto3.client('rds')

response = client.add_tags_to_resource(
    ResourceName='arn:aws:rds:us-east-2:585584209241:db:database-instance-01',
    Tags=[
        {
            'Key': 'Environment',
            'Value': 'Test',
        },
    ],
)
print(response)