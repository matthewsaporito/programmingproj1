#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 16:48:44 2020

@author: Matt
"""

def displayListOfGrades():
    DisplayGrades = computeFinalGrades()
    DisplayGrades = pd.DataFrame(DisplayGrades)
    lll=list(DisplayGrades.columns)
    DisplayGrades[lll[2:]] = pd.to_numeric(gdata[lll[2:]].stack(), errors='coerce').unstack()#data formatting from https://stackoverflow.com/questions/36814100/pandas-to-numeric-for-multiple-columns
    return DisplayGrades