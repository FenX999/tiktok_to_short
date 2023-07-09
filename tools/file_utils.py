import os


def make_path(spath, obj):
    return os.path.join(spath, obj)
    

def make_dir_or_get_path(spath , obj):
    path = make_path(spath, obj)
    try:
        os.mkdir(path)
        print(f'file created {path}')
    except FileExistsError:
        print('FileExistsError passing make_dir')
        pass
    return path
    
def generate_dir_list(path):
    return os.listdir(path)   

