import glob

parts = glob.glob('*.part[0-9]')
file_name = '.'.join(parts[0].split('.')[:-1])

with open(file_name, 'ab') as full_file:
    for pp in parts:
        with open(pp, 'rb') as p:
            full_file.write(p.read())