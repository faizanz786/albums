# Instagram part 2 with AWS SDK for python sample project

This goal of this project is to make a service similar to Instagram. 
The sole purpose is to learn how to connect different technologies and make a fully functioning product.

## Requirements

* Python 3
* Pipenv
* Insomnia
* Npm
* Node
* Amazon S3
* MongoDB
* MongoDB Compass

## Basic Configuration

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

## Features List
* [x] /upload route allows a user to upload an image to s3 storage
* [x] /photos route retrieves the image url from mongodb database
* [ ] upload component that will allow a user to upload an image with jpg ext
* [ ] display all the photos in the grid format with responsive UI

## Running the web server

```
pipenv install

pipenv shell

export FLASK_APP=services/app.py 

// For dev environment
export FLASK_ENV=development

flask run
```

## Running the client

```
npm install
npm run dev

// To run jest tests
npm run test
```
