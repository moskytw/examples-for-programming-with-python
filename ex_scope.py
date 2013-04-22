#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: ex_scope.py

x = 'global'

def f():
    if 1:
        x = 'local'
    return x

if __name__ == '__main__':
    print x
    print f()

