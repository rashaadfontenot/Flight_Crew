from pytube import YouTube
import boto3
import json
import pprint


def download_video():
    # Get YouTube link
    link = 'https://www.youtube.com/watch?v=F9U5UfKfDoI'
    yt = YouTube(link)
    title = yt.title
    stream = yt.streams.first()
    #pprint.pprint(stream)
    print('Downloading the video "{}" to your S3...'.format(title))

    # Create an S3 client
    s3 = boto3.client('s3')
    filename = str(title + '.mp4')
    bucket_name = 'pythonfun'
    stream.download()

    # S3 Upload
    upload_s3 = s3.upload_file(filename, bucket_name, filename)

    # Upload video to S3
    stream.download(output_path=upload_s3)
    print('Your video "{}" has finished downloading. Check your folder!'.format(title)) # add file location


download_video()







