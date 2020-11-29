# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 18:15:00 2020

@author: apek
"""
from pandas import isnull
from pandas import NA

def deNan(data):
    out = []  # creates an empty list
    
    for studentID, name, *assignments in data:
        Grades = [grade for grade in assignments if isnull(grade) == False]  # get rid of nans
        out.append([studentID, name, *Grades])  # adds the values to the list
            
    return out


