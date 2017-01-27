import boto3

### FUNCTION TO LIST ALL OPEN CASES #####
def lambda_handler(event, context):
    support_client = boto3.client('support')

    case_list = support_client.describe_cases()

    return case_list['cases']