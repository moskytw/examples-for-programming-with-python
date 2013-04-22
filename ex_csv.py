#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: ex_csv.py

import csv

with open('ex_csv.csv') as f:
    for row in csv.reader(f):
        print row
