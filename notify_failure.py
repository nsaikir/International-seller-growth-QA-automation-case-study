import boto3

def lambda_handler(event, context):
    sns = boto3.client('sns')
    message = "QA Test Failure: " + str(event)
    sns.publish(
        TopicArn='arn:aws:sns:us-east-1:123456789012:QAFailures',
        Message=message
    )
    return {"status": "notified"}
