import os
import logging

from . import data
from .data import UGIT_DIR

def write_tree(directory='.'):
    # logging.debug(f'write_tree with directory: {directory}')
    entries = []
    with os.scandir(directory) as it:
        for entry in it:
            # logging.debug(f'entry: {entry}')
            full_path = os.path.join(directory, entry.name)
            if is_ignored(full_path):
                continue
            if entry.is_file(follow_symlinks=False):
                type_ = 'blob'
                with open(full_path, 'rb') as f:
                    object_id = data.hash_object(f.read(), type_)
            elif entry.is_dir(follow_symlinks=False):
                type_ = 'tree'
                object_id = write_tree(full_path)
            entries.append((entry.name, object_id, type_))
    tree = ''.join(f'{type_} {object_id} {name}\n' for name,object_id,type_ in sorted(entries))
    # print(''.join(f'<{entry}>\n' for entry in sorted(entries)))
    print(tree, end='')
    tree_object_id = data.hash_object(tree.encode(), type_='tree')
    return tree_object_id
def is_ignored(path):
    basename = os.path.basename(path)
    ignored_dirs = [UGIT_DIR, 'venv']
    return basename in ignored_dirs or basename.startswith('.')