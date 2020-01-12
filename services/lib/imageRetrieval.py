from json import dumps
from bson import json_util

from dbOperations import fetch_data

def retrievePhotosFromDb():
    return dumps(list(fetch_data("photo", {})), default=json_util.default)
