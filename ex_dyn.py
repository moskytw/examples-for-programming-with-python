#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: ex_dyn.py

def dynsum(*seq):

    r = seq[0]
    for item in seq[1:]:
        r += item

    return r

if __name__ == '__main__':

    print dynsum(1, 2, 3)
    print dynsum('x', 'y', 'z')
