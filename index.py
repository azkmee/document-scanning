import boto3

client = boto3.client('textract')
print(client)