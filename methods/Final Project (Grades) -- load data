#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 16:05:56 2020

@author: Matt
"""


#Def FilterData
#load data, skipping invalid lines, return line where error occured and desc
#Column 0 must be a number between 10-60
#Column 1 must be a positive number
#Column 2 must be between 1-4

import os
import numpy as np
os.chdir('/Users/Matt/Desktop/')

#filename = 'testgrades(witherrors).csv'

def filecheck():
    #checks that user file exists loads as 'data'
    filename = str(input("Please enter The file you whish to load:"))
    data = [item.strip().split(",") for item in open(filename, 'r')]
    #print(data)
    return data[1:]

def validateRowLen(data):
    #checks that data file has 5 columns
    validated = []
    for i, item in enumerate(data):
        try:
            
            size = len(item)
            assert size == 5
            validated += [item]
            
        except AssertionError as e:
            pass
    return validated

def formatRow(i, j, k, l, m):
    
    if i == '':
        i = None
    else:
        i = str(i)
    if j == '':
        j = None
    else:
        j = str(j)  
    if k == '':
        k = None
    else:
        try:
            k = float(k)
        except:
            k = None           
    if l == '':
        l = None
    else:
        try:
            l = float(l)
        except:
            l = None 
    if m == '':
        m = None
    else:
        try:
            m = float(m)
        except:
            m = None 
        
    #k = None if k == '' else float(k)
    return (i, j, k, l, m)


def dataLoad():
    # pulls data from filecheck and filters to keep only valid rows from conditions above
    gdata = filecheck()
    data = gdata
    data = [formatRow(*item) for item in data]
    data = [formatRow(i, j, k, l, m) for i, j, k, l, m in data]
    #data = [(str(i), str(j), float(k), float(l), float(m)) for i, j, k, l, m in data]
    data = np.array([np.array(item) for item in data])
    
    #MUST FIND DUPLICATES IN THE SAME COLUMN
    #GRADES IN DATA SET MUST BE ONE OF 7 OPTIONS

     #data[data[:,2] not in (-3,0,2,4,7,10,12)]

    print(data)
    
    #error values by row, specifying error
    for i, item in enumerate(data):
        #StudentID, Name, Assignment1, Assignment2, Assignment3 = item 
        #StudentID, Name, Assignment1, Assignment2, Assignment3 = str(StudentID), str(Name), float(Assignment1), int(Assignment2), int(Assignment3)
        #if np.any(np.diff(np.sort(data, axis=0), axis=0) == 0):
            #print("There is a duplicate student ID in row {:d}".format(i+1))
        if data[data[:,2] not in (-3,0,2,4,7,10,12)]:
            print("Grade outside range at row {:d}".format(i+1))
    return data