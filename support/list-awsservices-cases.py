import boto3


client = boto3.client('support')


response =client.describe_services(
    serviceCodeList=[]
)
#print response['services']

for each_service in response['services']:
    #print each_service['code']
    print each_service['name']