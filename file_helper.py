import os

def is_dir(dirname):
    return os.path.isdir(dirname)

def is_file(filename):
    return os.path.isfile(filename)

def dir_path(source):
    fullpath = os.path.dirname(os.path.abspath(source))
    return fullpath

def get_filename(source):
    if not is_file(source):
        raise Exception("File not found")
    return os.path.splitext(os.path.basename(source))[0]

def get_fullpath(path, filename, file_ext):
    return os.path.join(path, filename + "." + file_ext)
