### FUNCTION TO LIST ALL OPEN CASES WITH SPECIFIC SECURITY LEVEL PASSED AS INPUT #####

####ALLOWED EVENT VALUES low, medium, high, urgent
def lambda_handler(event, context):
    support_client = boto3.client('support')

    case_list = support_client.describe_cases()

    for case in case_list['cases']:
        if case['severityCode']==event:
            return case_list['cases']
        else:
            return "Kindly enter a valid severity type"