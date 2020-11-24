#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 13:11:15 2020

@author: Matt
"""
import os
import numpy as np
import math as m
import pandas as pd
from pandas import isnull
from pandas import NA
from .roundgrade8 import roundGrades
from .utils import computeFinalGrades


os.chdir('/Users/Matt/Desktop/')

def displayGrades():
    
    filename = str(input("Please enter The file you wish to load:"))
    
    finalgrade = pd.DataFrame([line.strip().split(',') for line in open(filename, 'r')]) #pandas code from "zero" at testgrades(witherrors).csv"

    data = roundGrades()[1]
    db = pd.DataFrame(data)
    
    df = pd.concat([db,finalgrade],axis=1)

    return df.sort_values([1])
    
    
    
    #color = 'red' if val < 0 else 'black'
    #return 'color: %s' % color
    #s = df.style.applymap(color_negative_red)
    
    #return df

    

    
    # Sort by ascending student name
    #df.sort('student')
    # reverse ascending
    #df.sort('student', ascending=False)
    
    