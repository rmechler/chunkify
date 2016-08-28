
with open("big.txt", "w") as f:
    for x in xrange(1,1000001):
        f.write(str(x).zfill(999) + '\n')