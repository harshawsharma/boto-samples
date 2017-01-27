import boto3
lst = []
def lambda_handler(event, context):
    support_client = boto3.client('support')
    severity_levels = support_client.describe_severity_levels()
    for level in severity_levels['severityLevels']:
        lst.append(level['code'])
    return lst
