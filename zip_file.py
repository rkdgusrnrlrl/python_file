from zipfile import ZipFile

def zip_change_path():
    with ZipFile('print_hello.zip', 'w') as zz:
        zz.write('./dir/print_hello.py', arcname='print_hello.py')
