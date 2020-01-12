import hashlib

def hashString(string):
    return hashlib.sha224(string.encode('utf-8')).hexdigest()