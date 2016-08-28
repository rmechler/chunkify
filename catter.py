
with open('big2.txt', 'w') as f:
    with open("md5s.txt") as md5s:
        for md5 in md5s.readlines():
            print(md5.strip())
            with open('chunks/' + md5.strip()) as chunk:
                f.write(chunk.read())
