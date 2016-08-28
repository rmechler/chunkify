
with open('md5s.txt') as md5_file:
    md5s = md5_file.readlines()

with open('big2.txt', 'w') as f:
    for md5 in md5s:
        print(md5.strip())
        with open('chunks/' + md5.strip()) as chunk:
            for line in chunk.readlines():
                f.write(line)

with open('md5s.txt', 'w') as md5_file:
    md5_file.writelines(md5s)