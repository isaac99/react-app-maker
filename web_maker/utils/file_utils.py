import shutil


def read_file(file_path):
    with open(file_path, "r") as f:
        return f.read()

def copy_directory(src, dest):
    shutil.copytree(src, dest)