#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:51:15 2020

@author: Sara Sterlie
"""

def cvs_check():
    try:
        cvs_file = [item.strip().split() for item in open(filename, 'r')]
    except OSError:
        print("The file could not be found. Please Enter an existing file")
        continue
    
    with open(cvs_file, newline='') as f:
        reader = csv.reader(f)
        try:
            for row in reader:
                num_of_students = row
        except csv.Error as e:
            print('The file must be in CVS format')
return cvs_file, num_of_students