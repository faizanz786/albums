# Instagram part 2 with AWS SDK for python sample project

This goal of this project is to make a service similar to Instagram. 
The sole purpose is to learn how to connect different technologies and make a fully functioning product.

## Requirements

* Python 3
* Boto3
* Flask
* Insomnia
* Npm
* Node
* Amazon S3
* MongoDB
* MongoDB Compass

## Basic Configuration

Install boto3 and flask

```
pip install boto3 flask
```

Update aws.py in lib folder with following code:

```
aws_access_key_id = <your access key id>
aws_secret_access_key = <your secret key>
```

You will also need a REST client to make requests. Download Insomnia using:
```
https://insomnia.rest/download/
```
or
```    
brew cask install insomnia
```

Follow the instructions below to get MongoDB

```
https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/
```

To see your databases, collections and documents download MongoDB Compass

```
https://www.mongodb.com/download-center/compass
```


## Running the retrieval service

This sample application connects to Amazon's [Simple Storage Service (S3)](http://aws.amazon.com/s3),
and retrieves the uploaded file from S3. All you need to do is run the code:

```
python3 retrievalService.py
```

## Running the upload service

This sample application uploads the selected file to Amazon's [Simple Storage Service (S3)](http://aws.amazon.com/s3), and returns it's url. All you need to do is run the code and then make a post request in insomnia:

    python3 uploadService.py 

## Running the client

```
npm install
npm run dev

// To run jest tests
npm run test
```
