import boto3
from decimal import Decimal
import json
import urllib
import pprint
from collections import Counter


bucket = 'pythonfun'
rekognition = boto3.client('rekognition', 'us-east-1')


def get_response():
    label_job_id = 'b4306d5308cc018b04fac1e87c5df4193a34b16e0bd6f23415c6659d37bd112a'
    celeb_job_id = '2c1a72d253808484c55a2674b268af4047c8d6012ead2877c644994089b17d3b'
    label_response = rekognition.get_label_detection(JobId=label_job_id, MaxResults=100)
    celeb_response = rekognition.get_celebrity_recognition(JobId=celeb_job_id, MaxResults=100)

    label_list = []
    for label in label_response['Labels']:
        label_name = label['Label']['Name']
        label_list.append(label_name)
        label_list = list(set(label_list))
    print(label_list)

    celeb_list = []
    for Celebrity in celeb_response['Celebrities']:
        celebrity_name = Celebrity['Celebrity']['Name']
        celeb_list.append(celebrity_name)
        celeb_list = list(set(celeb_list))
    print(celeb_list)


    #pprint.pprint(label_response)
    #pprint.pprint(celeb_response)


get_response()