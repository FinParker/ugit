import os
import hashlib

UGIT_DIR = '.ugit'

def init():
	os.makedirs(UGIT_DIR, exist_ok=True)
	os.makedirs(f'{UGIT_DIR}/objects', exist_ok=True)

def hash_object(data):
	oid = hashlib.sha1(data).hexdigest()
	with open(f'{UGIT_DIR}/objects/{oid}', 'wb') as out:
		out.write(data)
	return oid