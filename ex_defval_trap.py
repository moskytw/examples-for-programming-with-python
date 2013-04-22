#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: ex_defval_trap.py

def f(items=[]):
    items.append(1)
    return items

if __name__ == '__main__':
    print f() # -> [1]
    print f() # -> [1, 1]
    print f() # -> [1, 1, 1]
