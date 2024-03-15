from os.path import isdir, isfile
import os, shutil


def d_to_d(dir1, dir2):
    if not os.path.exists(dir1) or not os.path.exists(dir2):
        raise Exception("Enter a valid path")
    shutil.rmtree(dir2)
    os.mkdir(dir2, 0o755)
    dirs = os.listdir(dir1)
    for obj in dirs:
        path = dir1 + obj
        if os.path.isdir(path):
            d_to_d(dir, dir2)
        if os.path.isfile(path):
            shutil.copy(path, dir2)


def main():
    d_to_d("/home/sean/Static Site/static/", "/home/sean/Static Site/public/")


main()
