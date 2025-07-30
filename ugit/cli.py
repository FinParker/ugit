import argparse
import logging
import os
import sys

from . import base, data

logging.basicConfig(level=logging.INFO)

def main ():
    args = parse_args()
    logging.debug('args: %s',args)
    args.func(args)

def parse_args():
    parser = argparse.ArgumentParser()

    # add optional arguments(-xxx, --yyy)
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')

    commands = parser.add_subparsers(dest='command')
    commands.required = True
    # ugit <command>
    # args.command = <command>

    init_parser = commands.add_parser('init')
    init_parser.set_defaults(func=init)
    # ugit init
    # args.func = init

    hash_object_parser = commands.add_parser('hash-object')
    hash_object_parser.set_defaults(func=hash_object)
    # add positional arguments
    hash_object_parser.add_argument('file')
    # ugit hash-object <file>
    # args.func = hash_object
    # args.file = <file>

    cat_file_parser = commands.add_parser('cat-file')
    cat_file_parser.set_defaults(func=cat_file)
    cat_file_parser.add_argument('object_id')
    # ugit cat-file <object_id>
    # args.func = cat_file
    # args.object_id = <object_id>

    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    return args

def init(args):import argparse
import logging
import os
import sys
from . import data

logging.basicConfig(level=logging.INFO)

def main ():
    args = parse_args()
    logging.debug('args: %s',args)
    args.func(args)

def parse_args():
    parser = argparse.ArgumentParser()

    # add optional arguments(-xxx, --yyy)
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')

    commands = parser.add_subparsers(dest='command')
    commands.required = True
    # ugit <command>
    # args.command = <command>

    init_parser = commands.add_parser('init')
    init_parser.set_defaults(func=init)
    # ugit init
    # args.func = init

    hash_object_parser = commands.add_parser('hash-object')
    hash_object_parser.set_defaults(func=hash_object)
    # add positional arguments
    hash_object_parser.add_argument('file')
    # ugit hash-object <file>
    # args.func = hash_object
    # args.file = <file>

    cat_file_parser = commands.add_parser('cat-file')
    cat_file_parser.set_defaults(func=cat_file)
    cat_file_parser.add_argument('object_id')
    # ugit cat-file <object_id>
    # args.func = cat_file
    # args.object_id = <object_id>

    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    return args

def init(args):
    data.init()

# default hash to type 'blob'
def hash_object(args):
    with open(args.file, 'rb') as f:
        print(f'file <{args.file}> hashed, SHA1 code:')
        print(data.hash_object(f.read()))

def cat_file(args):
    sys.stdout.flush()
    # don't expect any type, just output this object
    sys.stdout.buffer.write(data.get_object(args.object_id, expected=None))
    data.init()

# default hash to type 'blob'
def hash_object(args):
    with open(args.file, 'rb') as f:
        print(f'file <{args.file}> hashed, SHA1 code:')
        print(data.hash_object(f.read()))

def cat_file(args):
    sys.stdout.flush()
    # don't expect any type, just output this object
    sys.stdout.buffer.write(data.get_object(args.object_id, expected=None))