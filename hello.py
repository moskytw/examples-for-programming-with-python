#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: hello.py

def hello(name=None):

    if name:
        return 'Hello, %s!' % name
    else:
        return 'Hello, Python!'

if __name__ == '__main__':
    import sys

    if len(sys.argv) >= 2:
        print hello(sys.argv[1])
    else:
        print hello()


