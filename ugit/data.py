import os
import hashlib
import logging

UGIT_DIR = '.ugit'

def init():
    if os.path.exists(UGIT_DIR):
        raise FileExistsError(f'ugit repository already exists in {os.path.join(os.getcwd(), UGIT_DIR)}')
    
    logging.debug(f'Initialized empty ugit repository in {os.path.join(os.getcwd(), UGIT_DIR)}')
    os.makedirs(UGIT_DIR)
    os.makedirs(os.path.join(UGIT_DIR, 'objects'))

def hash_object(data):
    object_id = hashlib.sha1(data).hexdigest()
    with open(os.path.join(UGIT_DIR, 'objects', object_id), 'wb') as f:
        f.write(data)
    return object_id

def get_object(object_id):
    with open(os.path.join(UGIT_DIR, 'objects', object_id), 'rb') as f:
        content = f.read()
    print(f"File content (hex): {content.hex()}")
    return content
