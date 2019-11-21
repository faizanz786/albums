# Instagram part 2 with AWS SDK for python sample project
This goal of this project is to make a service similar to Instagram. 
The sole purpose is to learn how to connect different technologies and make a fully functioning product.

## Requirements
* Python 3
* boto3
* npm
* node
* Amazon S3


## Basic Configuration
Install boto3

```
pip install boto3
```

Update aws.py in lib folder with following code:

```
aws_access_key_id = <your access key id>
aws_secret_access_key = <your secret key>
```

## Running the S3 sample

This sample application connects to Amazon's [Simple Storage Service (S3)](http://aws.amazon.com/s3),
and retrieves the uploaded file from S3. All you need to do is run the code:

```
python3 retrievalService.py
```

## Running the client
```
npm install
npm run dev

// To run jest tests
npm run test
```