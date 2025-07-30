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

# The default type is going to be 'blob'
# since by default an object is a collection of bytes with no further semantic meaning.
def hash_object(data, type_='blob'):
    obj = type_.encode() + b'\x00' + data
    logging.debug(f"data is encoded to {obj}")
    object_id = hashlib.sha1(data).hexdigest()
    with open(os.path.join(UGIT_DIR, 'objects', object_id), 'wb') as f:
        f.write(obj)
    return object_id

def get_object(object_id, expected='blob'):
    with open(os.path.join(UGIT_DIR, 'objects', object_id), 'rb') as f:
        obj = f.read()
    type_, _,content = obj.partition(b'\x00')
    type_ = type_.decode()
    logging.debug(f"obj's type is {type_}")
    logging.debug(f"obj's content: {content}")
    
    # type check
    if expected is not None:
        assert type_ == expected, f'Expected {expected}, got {type_}'
    return content
