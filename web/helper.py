import hashlib

def hash_file_name(file_name):
    return hashlib.sha224(file_name.encode('utf-8')).hexdigest()
