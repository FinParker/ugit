import argparse
import logging

logging.basicConfig(level=logging.INFO)

def main ():
    args = parse_args()
    logging.debug('args: %s',args)
    args.func(args)

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--debug', action='store_true', help='Enable debug mode')

    commands = parser.add_subparsers(dest='command')
    commands.required = True
    # args.command = 'init'

    init_parser = commands.add_parser('init')
    init_parser.set_defaults(func=init)
    # args.func = init

    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    return args

def init(args):
    logging.debug('init process begin')