#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: ex_do.py

from operator import add, mul

def do(action, x, y):
    return action(x, y)

if __name__ == '__main__':
    print do(add, 10, 20)
    print do(mul, 10, 20)
