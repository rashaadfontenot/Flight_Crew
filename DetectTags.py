#! python3
import boto3
import json

kittyScott = "kittyscott.jpeg"
burger = "burgerFries.JPG"
jordan = "jordan.JPG"
spaceNeedle = "SpaceNeedle.jpg"
dori = "dori.JPG"
rashaad = "rashaad.JPG"







# if __name__ == "__main__":
#     fileName = kittyScott
#     bucket = 'pythonfun'
#     client=boto3.client('rekognition','us-east-1')
#
#     response = client.detect_faces(Image={'S3Object':{'Bucket':bucket,
#                                                       'Name':fileName}},Attributes=['ALL'])
#
#     print('Detected faces for ' + fileName)
#     for faceDetail in response['FaceDetails']:
#         print('The detected face is between ' + str(faceDetail['AgeRange']['Low'])
#               + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
#         print('Here are the other attributes:')
#         print(json.dumps(faceDetail, indent=4, sort_keys=True))

