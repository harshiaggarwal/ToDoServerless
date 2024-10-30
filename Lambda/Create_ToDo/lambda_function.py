import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ToDoTable')

def lambda_handler(event, context):
    data = json.loads(event['body'])
    item = {
        'id': str(uuid.uuid4()),  # Generates a unique ID
        'task': data['task'],
        'status': 'pending'       # Default status
    }
    table.put_item(Item=item)
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Task created!', 'item': item})
    }
