import boto3
from decimal import Decimal
import json
import urllib
import pprint
from collections import Counter


bucket = 'pythonfun'
rekognition = boto3.client('rekognition', 'us-east-1')


def get_response():
    get_response = rekognition.get_label_detection(
        JobId='c1b8de35a350abd82a4ed6d02801afcab51e6d041b893282322496845291f438',
        MaxResults=100
    )
    #pprint.pprint(get_response)
    for label in get_response['Labels']:
        tag = label['Label']['Name']
        print(tag)
        Counter(tag)

get_response()