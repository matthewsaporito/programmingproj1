#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 12:09:27 2020

@author: sarasterlie and Anna Pekarova"""


import os
import numpy as np
import pandas as pd


def validateData(data):
    validated = []
    for i, item in enumerate(data):
        try:
            
            size = len(item)
            assert size == 3, f"Error at row {i}. Data has wrong shape, expected N x 3, got {size}"
            temperature, growth_rate, bacteria = item
            assert 10 <= temperature <= 60, f"Error at row {i}. Temperature out of range, expected 10 <= temperature =< 10, got {temperature}"
            assert growth_rate > 0, f"Error at row {i}. Low growth rate, expected growth rate >= 0, got {growth_rate}"
            assert bacteria in {1, 2, 3, 4}, f"Error at row {i}. Unknown bacteria, expected bacteria in {1, 2, 3, 4}, got {bacteria}"
            
            validated += [item]
            
        except AssertionError as e:
            print(e)
            
    return validated

def loadData(filename=None, delimiter=" "):
    
    while True:
        filename = filename or str(input("Please enter The file you whish to load or 'quit':"))
        
        if filename == 'quit':
            return
        
        try:
            data = np.loadtxt(filename, delimiter=delimiter)
            data = validateData(data)
        except Exception as e:
            print(f"Error: {e}.")
            continue
     
        return data
        
        
        
 