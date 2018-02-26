import boto3
from decimal import Decimal
import json
import urllib
import pprint
from collections import Counter


bucket = 'pythonfun'
rekognition = boto3.client('rekognition', 'us-east-1')


def get_response():
    print('Enter the video ID below: ')
    get_response = rekognition.get_label_detection(
        JobId=input(),
        MaxResults=100
    )
    #pprint.pprint(get_response)
    for label in get_response['Labels']:
        tag = label['Label']['Name']
        print(tag)
        Counter(tag)

get_response()