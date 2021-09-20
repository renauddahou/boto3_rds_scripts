import boto3

client = boto3.client('rds')

response = client.apply_pending_maintenance_action(
    ApplyAction='db-upgrade',
    OptInType='immediate',
    ResourceIdentifier='arn:aws:rds:us-east-2:585584209241:db:database-instance-01'
)
print(response)