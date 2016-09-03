#!/usr/bin/env python

import chunkify

md5s, sizes = chunkify.get_chunk_list()

for md5, size in zip(md5s, sizes):
    print("{} {}".format(md5, size))
