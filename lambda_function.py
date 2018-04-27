import boto3
import os
import json
import sys

# Rekognition Detect Text Function
s3 = boto3.resource('s3')
def detectText(bucket,key):
    #try:
    filename = bucket['key']
    #file = "OCR-"
    #extension=".txt"
    #TxtKey= file+filename+extension
    TxtKey= filename
    rekognitionClient = boto3.client('rekognition', "us-east-1")
    response = rekognitionClient.detect_text(
            Image={
                'S3Object': {
                    'Bucket': bucket['bucket'],
                    'Name':  bucket['key'],
                }
            }
       )
      
    text = ''
    for t in response['TextDetections']:
        if t['Type'] == 'LINE':
            text = text+t['DetectedText']+' '
            s3.Bucket("ist440grp2ocr").put_object(Key=TxtKey, Body=text, ACL='public-read', ContentType='text/plain')
    output = {
        "bucket": "ist440grp2ocr",
        "key": TxtKey
    }
    return output
       
    #except:
    #    output = {
    #        "failed": "true"
    #    }
    #return output