# Instagram part 2 with AWS SDK for python sample project
This goal of this project is to make a service similar to Instagram. 
The sole purpose is to learn how to connect different technologies and make a fully functioning product.

## Requirements

This sample project depends on `boto3` and `flask`, the AWS SDK and web framework for Python, and requires Python 2.6.5+, 2.7, 3.3, 3.4, or 3.5. You can install `boto3` and `flask` using pip:

    pip install boto3
    pip install flask

You will also need a REST client to make requests. Download Insomnia using:

    https://insomnia.rest/download/
or
    
    brew cask install insomnia


## Basic Configuration

You need to set up your AWS security credentials before the sample code is able
to connect to AWS. You can do this by creating a file named "credentials" at ~/.aws/ 
(`C:\Users\USER_NAME\.aws\` for Windows users) and saving the following lines in the file:

    [default]
    aws_access_key_id = <your access key id>
    aws_secret_access_key = <your secret key>

See the [Security Credentials](http://aws.amazon.com/security-credentials) page
for more information on getting your keys. For more information on configuring `boto3`,
check out the Quickstart section in the [developer guide](https://boto3.readthedocs.org/en/latest/guide/quickstart.html).

## Running the retrieval service

This sample application connects to Amazon's [Simple Storage Service (S3)](http://aws.amazon.com/s3),
and retrieves the uploaded file from S3. All you need to do is run the code:

    python3 retrievalService.py 

## Running the upload service

This sample application uploads the selected file to Amazon's [Simple Storage Service (S3)](http://aws.amazon.com/s3), and returns it's url. All you need to do is run the code and then make a post request in insomnia:

    python3 uploadService.py 