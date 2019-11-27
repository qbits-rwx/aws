import boto3
# create a ssh-key for user benjamin

client = boto3.client('ec2')

response = client.create_key_pair(
    KeyName='pihole',
    DryRun=False
)




