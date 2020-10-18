'''
Author: Khai Fahmi
Description: Helper functions related to AWS services interaction
'''

import boto3
from botocore.exceptions import ClientError

def save_to_db(node_id=None, inference_type, confidence, table_name='cough-detection'):
    # ts will represent the PARTITION KEY
    ts = datetime.now()
    ts = ts.strftime("%d-%m-%Y %H:%M:%S")

    # initialise object to be sent
    data = {
        'ts': ts,
        'inference_type': inference_type,
        'confidence': confidence
    }

    table = boto3.resource('dynamodb', region_name='ap-southeast-2').Table(table_name)

    try:
        result = table.put_item(
            Item = data
        )
        print('Inference upload successful')
    except Exception as e:
        print('Inference upload fail: aws_controller.save_to_db()')

    return result