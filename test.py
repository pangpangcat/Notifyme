

import boto3
import json
import numpy as np

# data = np.arange(5)
# payload = [{'id':int(x)} for x in data]
# payloadStr = json.dumps(payload)
# payloadBytesArr = bytes(payloadStr, encoding='utf8')

client = boto3.client('lambda')
n = 3000
for i in range(n):
    response = client.invoke(
        FunctionName='myLambdaTest',
        InvocationType="Event",
        Payload=json.dumps({'id':i})
    )


dynamodb = boto3.resource('dynamodb',region_name='us-east-1')

table = dynamodb.Table('testtime')
