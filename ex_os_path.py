#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: ex_os_path.py

from os import walk
from os.path import join

def list_files(path):
    paths = []
    for root, dir_names, file_names in walk(path):
        for file_name in file_names:
            paths.append(join(root, file_name))
    return paths

if __name__ == '__main__':

    import sys
    from os.path import abspath, dirname

    if len(sys.argv) == 2:
        path = abspath(dirname(sys.argv[1]))
        for path in list_files(path):
            print path
    else:
        print 'It requires a path as argument.'
