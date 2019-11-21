from flask import Flask, request
import boto3
import sys
import os
sys.path.insert(1, os.path.join(os.path.dirname(__file__), os.pardir, 'lib'))

from imageStorage import uploadPhotoAndReturnUrl

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
        output = uploadPhotoAndReturnUrl(bucketName, file)
        return output

if __name__ == "__main__":
    app.run(debug=True)

