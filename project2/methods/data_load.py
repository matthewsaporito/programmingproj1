#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 16:46:59 2020

@author: Matt Saporito
"""


import os
import numpy as np
import pandas as pd
from pandas import isnull
os.chdir('/Users/Matt/Desktop/')

#filename = 'testgrades(witherrors).csv'

def filecheck():
    #checks that user file exists loads as 'data'
    filename = str(input("Please enter The file you wish to load:"))
    
    try:
        # data = np.loadtxt(filename, delimiter=" ")
        data = pd.DataFrame([line.strip().split(',') for line in open(filename, 'r')]) #converts csv file to pandas dataframe
        return data[1:]#returns data excluding headers
    except OSError:
        print("The file could not be found. Please Enter an existing file")
        return filecheck()
    except Exception as e:
        print(e)
        return filecheck()


def dataLoad(gdata=None): #converts columns 2 onward to numeric for use in claculations
    gdata = filecheck()
    lll=list(gdata.columns) #gets list of column numbers
    gdata[lll[2:]] = pd.to_numeric(gdata[lll[2:]].stack(), errors='coerce').unstack()#data formatting from https://stackoverflow.com/questions/36814100/pandas-to-numeric-for-multiple-columns
    return gdata


def filterData(gdata, log=True):
     
    
    dfcol1 = pd.DataFrame(gdata, columns =[0])
    duplicaterow = dfcol1[dfcol1.duplicated()]  
    if log:  #will only print error rows in a later module if log is true
        print("\nThe following rows contain duplicate student IDs, the row with the first duplicate occurence will be kept:\n", "\n", duplicaterow.to_string(header = False))
    data = gdata[gdata[0].notnull()].drop_duplicates(subset=0, keep='first') #pandas code from https://stackoverflow.com/questions/45655080/remove-duplicates-using-pandas-python
     
    print("\n The data has been filtered, now the number of students is {}.\n".format(len(data.index)))
    
    if log:  #will only print error rows in a later module if log is true     
        colnumber=len(list(gdata.columns))
        datacols = gdata.iloc[:,range(2,colnumber)]  # https://python-forum.io/Thread-Iterating-over-pandas-df-to-check-for-values-out-of-range?page=2
        rownumber = len(gdata.index)
  
        rownum =0
        for rownumber in datacols.values:
            for i in rownumber:
                if (i < -3 or i > 12):
                    print("We found a grade outside range at row number {}, the grade is {}.".format(rownum+2, i))
            rownum+=1
        
    data = data.values.tolist()
    return data
    

