import shutil

def backup_file(path):
    shutil.copy(path, path + ".backup")