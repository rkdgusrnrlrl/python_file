import sys

file = sys.argv[1]

CHUNK_SIZE = 1000 * 50000
file_number = 1
with open(file, 'rb') as f:
    chunk = f.read(CHUNK_SIZE)
    while chunk:
        with open('%s.part%d' % (file, file_number), 'wb') as chunk_file:
            chunk_file.write(chunk)
        file_number += 1
        chunk = f.read(CHUNK_SIZE)