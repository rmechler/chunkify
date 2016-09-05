
import subprocess
import random
import hashlib
import os

CHUNK_SIZE = 100000
MD5_LIST_FILE = 'md5s.txt'

def randint(end):
    """
    """
    return random.randint(0, end-1)

def make_test_file(filename, linesize=1000, numlines=1000, chunksize=CHUNK_SIZE):
    """
    """
    with open(filename, "w") as f:
        for x in xrange(1, numlines+1):
            f.write(str(x).zfill(linesize-1) + '\n')

def make_diff_file(old, new, adds=1, deletes=0, changes=0, per_change_limit=1):
    """
    """
    with open(old) as f:
        lines = f.readlines()

    num_lines = len(lines)

    for x in xrange(adds):
        index = randint(num_lines)
        for y in xrange(randint(per_change_limit)+1):
            newline = 'blah\n'
            lines.insert(index, newline)

    for x in xrange(deletes):
        index = randint(num_lines)
        for y in xrange(randint(per_change_limit)+1):
            lines.pop(index)

    for x in xrange(changes):
        index = randint(num_lines)
        for y in xrange(randint(per_change_limit)+1):
            lines.pop(index)
        for y in xrange(randint(per_change_limit)+1):
            newline = 'blah\n'
            lines.insert(index, newline)

        # newline = 'blah\n'
        # lines[randint(num_lines)] = newline

    with open(new, 'w') as f:
        f.writelines(lines)

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

def get_chunk_md5s():
    """
    """
    with open(MD5_LIST_FILE) as md5_file:
        return [md5.strip() for md5 in md5_file.readlines()]

def get_chunk_sizes(md5s):
    """
    """
    return [os.path.getsize("chunks/" + md5)for md5 in md5s]

def assemble_chunks_to_file(filename, chunksdir='chunks'):
    """
    """
    with open(filename, 'w') as f:
        for md5 in get_chunk_md5s():
            print(md5.strip())
            with open(os.path.join(chunksdir, md5.strip())) as chunk:
                for line in chunk.readlines():
                    f.write(line)

    # with open(MD5_LIST_FILE, 'w') as md5_file:
    #     md5_file.writelines(md5s)

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


