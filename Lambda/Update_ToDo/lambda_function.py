import json
import boto3

def lambda_handler(event, context):
    # Retrieve task ID from path parameters
    task_id = None
    if 'pathParameters' in event and event['pathParameters']:
        task_id = event['pathParameters']['id']


    # Parse the request body for the status
    try:
        request_body = json.loads(event['body'])
        status = request_body.get('status')
    except (KeyError, json.JSONDecodeError):
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid request body'})
        }
    
    # Connect to DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('ToDoTable')

    try:
        # Update the item in DynamoDB
        table.update_item(
            Key={'id': task_id},
            UpdateExpression='SET #s = :val1',
            ExpressionAttributeNames={'#s': 'status'},
            ExpressionAttributeValues={':val1': status}
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Task updated successfully!'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }
