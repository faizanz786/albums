# Import the SDK
import boto3

s3client = boto3.client('s3')

# Everything uploaded to Amazon S3 must belong to a bucket. These buckets are
# in the global namespace, and must have a unique name.
#
# For more information about bucket name restrictions, see:
# http://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html
bucket_name = 'faizan-profile-1'

# Now find the specified bucket in your list of buckets.

list_buckets_resp = s3client.list_buckets()
for bucket in list_buckets_resp['Buckets']:
    if bucket['Name'] == bucket_name:
        print('(Just created) --> {} - there since {}'.format(
            bucket['Name'], bucket['CreationDate']))

# Using the client, you can generate a pre-signed URL that you can give
# others to securely share the object without making it publicly accessible.
# By default, the generated URL will expire and no longer function after one
# hour. You can change the expiration to be from 1 second to 604800 seconds
# (1 week).
object_key = 'IMG_3102.JPG'
url = s3client.generate_presigned_url(
    'get_object', {'Bucket': bucket_name, 'Key': object_key})
print('\nTry this URL in your browser to download the object:')
print(url)