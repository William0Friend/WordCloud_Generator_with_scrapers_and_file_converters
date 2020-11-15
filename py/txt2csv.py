# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 16:37:16 2020

@author: willf
"""
import csv
name = 'test2'
name_csv = 'test2.csv'
try:
    with open('clean.txt','r', encoding='utf-8', errors='ignore') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split("\t")for line in stripped if line)
        with open(name_csv, 'w', encoding='utf-8') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(lines)
except AssertionError as e:
    print(str(e))   
except UnicodeEncodeError as e:
    print(str(e))