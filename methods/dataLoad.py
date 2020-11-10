#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 13:49:11 2020

@author: Matt Saporito
"""

#Def FilterData
#load data, skipping invalid lines, return line where error occured and desc
#Column 0 must be a number between 10-60
#Column 1 must be a positive number
#Column 2 must be between 1-4

import os
import numpy as np

#os.chdir("/Users/Matt/Desktop/Data files for exercise modules 4")

#filename = 'test.txt'



def filecheck():
    #checks that user file exists loads as 'data'
    filename = str(input("Please enter The file you whish to load:"))
    try:
        data = np.loadtxt(filename, delimiter=" ")
        return data
    except OSError:
        print("The file could not be found. Please Enter an existing file")
        return filecheck()
    
def validateData(data):
    #checks that data file has 3 columns
    validated = []
    for i, item in enumerate(data):
        try:
            
            size = len(item)
            assert size == 3
            
            validated += [item]
            
        except AssertionError as e:
            pass
        
        validated = data
    return data

def dataLoad():
    # pulls data from filecheck and filters to keep only valid rows from conditions above
    bdata = filecheck()
        
    data = np.array(bdata)
    
    data = data[data[:,0]>10]
    data = data[data[:,0]<60]
    data = data[data[:,1]>0]
    data = data[data[:,2]>=1]
    data = data[data[:,2]<=4]
    data = validateData(data)
    
    #print(data)
    
    #error values by row, specifying error
    for i in range(len(bdata)):
        if bdata[i,0]<10:
            print("Temp is too low in row {:d}".format(i+1))
        if bdata[i,0]>60:
            print("Temp is too high in row {:d}".format(i+1))
        if bdata[i,1]<0:
            print("invalid growth rate in row {:d}".format(i+1))  
        if not np.any(int(bdata[i,2]) == np.array([1,2,3,4])):
            print("invalid bacteria type in row {:d}".format(i+1))
        if not len(bdata[i]) == 3:
            print("data has wrong shape at row {i}, expected N x 3, got {size}")

    return data
#print(data)

# data = dataLoad(filename)


        

        