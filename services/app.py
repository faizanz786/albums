import sys
import os
sys.path.insert(1, os.path.join(os.path.dirname(__file__), os.pardir, 'services/lib'))

from imageStorage import insertPhotoInDb
from imageRetrieval import retrievePhotosFromDb
from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    if "user_file" not in request.files:
        return "No user_file key in request.files"
    
    file = request.files["user_file"]

    if file.filename == "":
        return "Please select a file"

    if file:
        bucketName = 'faizan-profile-1'
        output = insertPhotoInDb(bucketName, file)
        return output

@app.route('/photos', methods=['POST'])
def retrievePhotos():
    return retrievePhotosFromDb()