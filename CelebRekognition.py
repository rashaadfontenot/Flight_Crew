from pytube import YouTube
import boto3
import json
import pprint
import urllib.parse


def download_video():
    # Get YouTube link
    print('Enter YouTube link below: ')
    link = input()
    yt = YouTube(link)
    title = yt.title.replace("'", '')
    print(title)
    stream = yt.streams.first()
    pprint.pprint(stream)
    print('Downloading the video "{}" to your S3...'.format(title))

    # Create an S3 client
    s3 = boto3.client('s3')
    filename = str(title + '.mp4').replace("'", '+')
    print('filename made')
    bucket_name = 'pythonfun'
    print('bucket made')
    stream.download()
    print('download complete')

    # S3 Upload
    upload_s3 = s3.upload_file(filename, bucket_name, filename)
    print('upload to s3')

    # Upload video to S3
    stream.download(output_path=upload_s3)
    print('Your video "{}" has finished downloading. Check your folder!'.format(title)) # add file location

    # Send Video to celebrity rekognition API
    rekognition = boto3.client('rekognition', 'us-east-1')
    response = rekognition.start_celebrity_recognition(Video={"S3Object": {"Bucket": bucket_name, "Name": filename}})
    job_id = response['JobId']
    print(job_id)


download_video()