### FUNCTION TO LIST ALL CASES, OPEN AND CLOSED #####
def lambda_handler(event, context):
    support_client = boto3.client('support')

    case_list = support_client.describe_cases(
        includeResolvedCases=True
    )

    return case_list['cases']

