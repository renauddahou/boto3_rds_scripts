import boto3
from datetime import datetime

client = boto3.client('rds')
response = client.restore_db_instance_to_point_in_time(
    RestoreTime=datetime(2021, 9, 15),
    SourceDBInstanceIdentifier='database-instance-01',
    TargetDBInstanceIdentifier='restored-db-01'
)
print(response)