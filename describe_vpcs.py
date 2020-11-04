import json
import boto3

client=boto3.client('ec2')

json_response=json.dumps(client.describe_vpcs(Filters=[{'Name': 'tag:Name', 'Values': ['sudharsan-vpc1']}], VpcIds=['vpc-026bcb174901014ac']), indent=4)
#json_response=json.dumps(client.describe_vpcs(VpcIds=['vpc-026bcb174901014ac']), indent=4)
data=json.loads(json_response)
x=data['Vpcs']
y=dict(x[0])
print("Please find the VPC details")
print(f"VpcId is: " +  y['VpcId'])
print(f"State is: " +  y['State'])
print(f"CidrBlock is: " +  y['CidrBlock'])
print(f"OwnerId is: " +  y['OwnerId'])
