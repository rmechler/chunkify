
import subprocess
import hashlib
import os

CHUNK_SIZE = 100000
MD5_LIST_FILE = 'md5s.txt'

def diff(file1, file2):
    """
    """
    # TODO: piping to cat so it won't return error code thus exception... need a better way
    diffs = [line for line in subprocess.check_output("diff {} {} | cat".format(file1, file2), shell=True).split('\n')
             if line and not any(line.startswith(c) for c in ['>', '<', '-'])]

    return diffs


def write_chunk(content, md5s_file):
    """
    """
    md5 = hashlib.md5(content).hexdigest()
    with open("chunks/" + md5, 'w') as chunk_file:
        chunk_file.write(content)
    md5s_file.write(md5 + '\n')


def get_chunk_list():
    """
    """
    with open(MD5_LIST_FILE) as md5_file:
        md5s = [md5.strip() for md5 in md5_file.readlines()]

    sizes = [os.path.getsize("chunks/" + md5)for md5 in md5s]

    return md5s, sizes


def make_chunks(filename):
    """
    """
    content = ''
    size = 0
    with open(filename) as f:
        with open(MD5_LIST_FILE, 'w') as md5_file:
            while True:
                line = f.readline()
                if not line:
                    if content:
                        write_chunk(content, md5_file)
                    break
                size += len(line)
                content += line
                if size >= CHUNK_SIZE:
                    write_chunk(content, md5_file)
                    content = ''
                    size = 0


