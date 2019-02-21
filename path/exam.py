from os import path

parent_path = path.dirname(path.dirname(path.abspath(__file__)))
print('parent path: %s' % parent_path)
this_dir_name = path.basename(path.dirname(path.abspath(__file__)))
print('this dir name: %s' % this_dir_name)
make_path = path.join(parent_path, 'dir1')
print('make path: %s' % make_path)
