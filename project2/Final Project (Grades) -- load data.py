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
    return data[1:]

def formatRow(i=None, j=None, *grades):
    if i == '':
        i = None
    else:
        i = str(i)
    if j == '':
        j = None
    else:
        j = str(j)  
    
    for arg in grades:
        try:
            arg = float(arg)
        except:
            arg = None  
            
    #k = None if k == '' else float(k)
    return (i, j, *grades)


def dataLoad():
    # pulls data from filecheck and filters to keep only valid rows from conditions above
    gdata = filecheck()
    data = gdata
    data = [formatRow(i, j, *grades) for i, j, *grades in data]
    
    #error values by row, specifying error
    filteredData = []  # creates an empty list
    for i, row in enumerate(data):
        
        StudentID, Name, *grades = row
        
        #if any(diff(sort(data, axis=0), axis=0) == 0):
            #print("There is a duplicate student ID in row {:d}".format(i+1))
            
        for grade in grades:  
            #if int(grade) not in (-3,0,2,4,7,10,12):
                #print("Grade outside range at row {:d}, {}".format(i+1, grade))
            #else:
             #   filteredData.append(row)  # if the values are within a range in saves the row into the
        #return filteredData
    
            try:
                assert not -3 < grade > 12  # tries if the value is in the range
            except:
                print("Grade outside range at row {:d}, {}".format(i+1, grades))  
                break # if not breaks the loop
        else:
            filteredData.append(row)  # if the values are within a range in saves the row into the list
            
        return filteredData