#! python3
import boto3
import json

kittyScott = "kittyscott.jpeg"
burger = "burgerFries.JPG"
jordan = "jordan.JPG"
spaceNeedle = "SpaceNeedle.jpg"
dori = "dori.JPG"
rashaad = "rashaad.JPG"
ecca = 'Emerald City Creative Arts Fall Class Ad.mp4'







if __name__ == "__main__":
    fileName = ecca
    bucket = 'pythonfun'
    client=boto3.client('rekognition','us-east-1')

    #response = client.detect_faces(Image={'S3Object':{'Bucket':bucket,
                                                    #  'Name':fileName}},Attributes=['ALL'])

    #response2 = client.start_label_detection(Video={'S3Object':{'Bucket':bucket,
     #                                                 'Name':fileName}})

    response = client.start_label_detection(
        Video={
            'S3Object': {
                'Bucket': bucket,
                'Name': fileName
            }
        },
        ClientRequestToken='string',
        MinConfidence=70
    )

    # print('Detected faces for ' + fileName)
    # for faceDetail in response['FaceDetails']:
    #     print('The detected face is between ' + str(faceDetail['AgeRange']['Low'])
    #           + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
    #     print('Here are the other attributes:')
    #     print(json.dumps(faceDetail, indent=4, sort_keys=True))


    print('Detected faces for ' + fileName)
    for faceDetail in response2['FaceDetails']:

