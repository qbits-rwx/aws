import boto3
import sys
# create a ssh-key for account benjamin

client = boto3.client('ec2')

def main():
  response = client.create_key_pair(
  KeyName='bar',
  DryRun=False
  )
  for key, value in response.items():
      print (key, value)

if __name__=="__main__":
    main()







