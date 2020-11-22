#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 17:33:42 2020

@author: Matt
"""


import os
import numpy as np
import pandas as pd
os.chdir('/Users/Matt/Desktop/')

#filename = 'testgrades(witherrors).csv'

def filecheck():
    #checks that user file exists loads as 'data'
    filename = str(input("Please enter The file you wish to load:"))
    data = pd.DataFrame([line.strip().split(',') for line in open(filename, 'r')]) #pandas code from "zero" at testgrades(witherrors).csv"
    return data[1:] 



def dataLoad():
    # pulls data from filecheck and filters to keep only valid rows from conditions above
    gdata = filecheck()
    lll=list(gdata.columns)
    gdata[lll[2:]] = pd.to_numeric(gdata[lll[2:]].stack(), errors='coerce').unstack()#data formatting from https://stackoverflow.com/questions/36814100/pandas-to-numeric-for-multiple-columns
    
    return gdata



def filterData():
    
    gdata = dataLoad()
    dfcol1 = pd.DataFrame(gdata, columns =[0])
    duplicaterow = dfcol1[dfcol1.duplicated()]
    while True:
        print("The following rows contain duplicate student IDs, the row with the first duplicate occurence will be kept:\n", duplicaterow.to_string(header = False))
        try:
            selection = input("Would you like to remove the rows with duplicate student IDs, keeping the first row of the occurrence?  Please enter ""Y"" or ""N"": " )

            if selection == selection.capitalize():#if user types 1, programs asks user to choose a bactaria filter.
                data = gdata[gdata[0].notnull()].drop_duplicates(subset=0, keep='first') #pandas code from https://stackoverflow.com/questions/45655080/remove-duplicates-using-pandas-python
            elif selection == selection.capitalize():
                break
            else:
                print("please either enter y or n")
                continue
