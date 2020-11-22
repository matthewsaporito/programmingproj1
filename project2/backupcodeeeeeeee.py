#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 17:07:08 2020

@author: Matt
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 16:46:59 2020

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
    gdata[lll[2:]] = pd.to_numeric(gdata[lll[2:]].stack(), errors='coerce').unstack()
    
    return gdata



def filterData():
    
    gdata = dataLoad()
    dfcol1 = pd.DataFrame(gdata, columns =[0])
    duplicaterow = dfcol1[dfcol1.duplicated()]
    print("The following rows contain duplicate student IDs, the row with the first duplicate occurence will be kept:\n", duplicaterow.to_string(header = False))
    data = gdata[gdata[0].notnull()].drop_duplicates(subset=0, keep='first') #pandas code from https://stackoverflow.com/questions/45655080/remove-duplicates-using-pandas-python
    
    datadf = pd.DataFrame(data.iloc[:,2:])
    print(datadf)
    print(datadf.dtypes)
    
    #data[cols] = data[cols].apply(pd.to_numeric, errors='coerce', axis=1)
    lll=list(data.columns)
    data[lll[2:]] = pd.to_numeric(data[lll[2:]].stack(), errors='coerce').unstack()
    #data.iloc[2:] = data.iloc[2:].astype(float)
    print(data.dtypes)
    print(data)
    
    
    print(data)
    #ppp = data.values.tolist()
    
    #print(ppp)
    
    #for i in range(len(data.columns[2:])):
    #gradefail = []
    #for row in data.iloc[:,2:]:
        #if row ==2:
            #print("FIVE")
            
        #gradefail+=[row]
        
    #return(gradefail, data) 
         
    
    
    
    
    
    
    
        #datadf = pd.DataFrame(data.iloc[:,2:])
    #print(datadf)
    #print(datadf.dtypes)
    
    #data[cols] = data[cols].apply(pd.to_numeric, errors='coerce', axis=1)
    #lll=list(data.columns)
    #data[lll[2:]] = pd.to_numeric(data[lll[2:]].stack(), errors='coerce').unstack()
    #data.iloc[2:] = data.iloc[2:].astype(float)

    #ppp = data.values.tolist()
    
    #print(ppp)
    
    #for i in range(len(data.columns[2:])):
    #gradefail = []
    #for row in data.iloc[:,2:]:
        #if row ==2:
            #print("FIVE")
            
        #gradefail+=[row]
        
    #return(gradefail, data)