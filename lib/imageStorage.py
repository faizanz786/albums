import boto3
from aws import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

s3Client = None

def getS3Client():
    global s3Client
    if s3Client is None:
        if not AWS_ACCESS_KEY_ID:
            print('AWS access key id is not defined. Please update aws.py in lib folder.')
            return None
        if not AWS_SECRET_ACCESS_KEY:
            print('AWS secret access key is not defined. Please update aws.py in lib folder.')
            return None
        s3Client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    return s3Client

def retrievePhotoURL(bucketName, photoName):
    s3 = getS3Client()
    if (s3 is None) :
        return None
    url = s3.generate_presigned_url('get_object', {'Bucket': bucketName, 'Key': photoName})
    return url

def uploadPhotoAndReturnUrl(bucketName, file):
    s3 = getS3Client()
    if (s3 is None) :
        return None
    s3.put_object(Bucket=bucketName, Key=file.filename, Body=file, ContentType='image/jpeg')
    return retrievePhotoURL(bucketName, file.filename)