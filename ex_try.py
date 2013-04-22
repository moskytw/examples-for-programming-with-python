#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: ex_try.py

def take_int(prompt='Give me a int: '):
    while 1:
        try:
            user_input = int(raw_input(prompt))
        except ValueError, e:
            print 'It is not a int!'
        else:
            return user_input

if __name__ == '__main__':
    x = take_int()
    print 'I got a int from user: %d' % x
