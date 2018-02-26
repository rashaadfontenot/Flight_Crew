import boto3
from decimal import Decimal
import json
import urllib



filename = 'LeBron James Historic Block on Andre Iguodala From All Angles.mp4'
bucket = 'pythonfun'
rekognition = boto3.client('rekognition', 'us-east-1')


def detect_faces(bucket, filename):
    response = rekognition.start_label_detection(Video={"S3Object": {"Bucket": bucket,
                                                                     "Name": filename}})
    job_id = response['JobId']
    print(job_id)


detect_faces(bucket, filename)


