import os
import sys
import hashlib
from datetime import datetime

output_file = 'hashes.txt'
file_hash_list = []
BUF_SIZE = 4096


def current_time():
    return datetime.now()


def hash_dir_tree(parent: str):
    """iterates through file tree and hashes files"""
    for root, dirs, files in os.walk(parent):
        for file in files:
            abs_path = os.path.join(root, file)
            algo = hashlib.sha256()

            with open(abs_path, 'rb') as f:
                while True:
                    data = f.read(algo.block_size)
                    if not data:
                        break
                    algo.update(data)
                file_hash_list.append(f'{algo.hexdigest()}\t{abs_path}\t{current_time()}')


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("""
        improper use
        
        Example:
        python3 ./evisure.py /path/to/parent/directory
        """)
        sys.exit(1)

    path_to = sys.argv[1]

    hash_dir_tree(path_to)

    with open(output_file, 'a') as of:
        for line in file_hash_list:
            of.write(line + '\n')

    print(f"hashes dump to {output_file}")
