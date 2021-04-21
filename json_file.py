import json
from file_helper import dir_path, get_filename, get_fullpath

def write(source, obj, filename):
    path = dir_path(source)
    fullpath = get_fullpath(path, filename, 'json')
    print(obj)
    with open(fullpath, 'w', encoding='utf8') as f:
        json.dump(obj, f, ensure_ascii=False, separators=(',', ': '), indent=4)
