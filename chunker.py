import hashlib

CHUNK_SIZE = 100000

content = ''
size = 0
with open('big.txt') as f:
    with open('md5s.txt', 'w') as md5s:
        while True:
            line = f.readline()
            if not line:
                if content:
                    md5 = hashlib.md5(content).hexdigest()
                    with open("chunks/" + md5, 'w') as chunk_file:
                        chunk_file.write(content)
                    md5s.write(md5 + '\n')
                break
            size += len(line)
            content += line
            if size >= CHUNK_SIZE:
                md5 = hashlib.md5(content).hexdigest()
                with open("chunks/" + md5, 'w') as chunk_file:
                    chunk_file.write(content)
                md5s.write(md5 + '\n')
                content = ''
                size = 0




