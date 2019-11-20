# Enable import from lib folder
import sys
import os
sys.path.insert(1, os.path.join(os.path.dirname(__file__), os.pardir, 'lib'))

from imageStorage import retrievePhotoURL

bucketName = 'faizan-profile-1'
photoName = 'IMG_3102.JPG'
url = retrievePhotoURL(bucketName, photoName)
if (url is None):
    print('Unable to retrieve the photo url')
else:
    print('Photo URL: {url}'.format(url = url))