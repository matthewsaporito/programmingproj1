#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 08:59:45 2020

@author: Sara Sterlie
"""
import sys

def anykey():
    print('Press any key to exit')
    a = input('')
    if a =='':
        sys.exit()
anykey()

