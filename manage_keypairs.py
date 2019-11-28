import boto3
import sys
# create / or delete a ssh-key for account benjamin

client = boto3.client('ec2')

def main():
  action = sys.argv[1] # create | delete | list  keypair
  if action in 'create':
      response = client.create_key_pair(
      KeyName= sys.argv[2],
      DryRun=False
      )
      with open("keyfile.txt", "w") as file:
          for key, value in response.items():
              keyfilecontent = key + ": " + value + "\n"
              file.write(keyfilecontent)
        # print (key, value)
     
  if action in 'delete':
      response = client.delete_key_pair(
          KeyName = sys.argv[2]
      )
      print(response)

  if action in 'list':
      response = client.describe_key_pairs()
      print(response) 
  elif action not in 'create' or 'delete' or 'list':
      print(sys.argv[0] + ' ' + 'use create | delete | list as an option')


if __name__=="__main__":
    main()







