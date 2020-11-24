#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:46:47 2020

@author: Sara Sterlie
"""
import numpy as np
import math as m
import pandas as pd
from pandas import isnull
from pandas import NA
from data_load import filterData


def roundGrades():
    
    data = filterData(log=False)

    for g, (studentID, name, *grades) in enumerate(data):
        for k, i in enumerate(grades):
            if (i <= 12 and i >= 11):
                data[g][k + 2] = 12
            elif (i < 11 and i >= 8.5):
                data[g][k + 2] = 10
            elif (i < 8.5 and i >= 5.5):
                data[g][k + 2] = 7
            elif (i < 5.5 and i >= 3):
                data[g][k + 2] = 4
            elif (i < 3 and i >= 1):
                data[g][k + 2] = 2
            elif (i < 1 and i >= -1.5):
                data[g][k + 2] = 0
            elif (i <-1.5 and i >= -3):
                data[g][k + 2] = -3
            else:
                data[g][k + 2] = NA
             
                data = np.array(data)   
                bdata = data[:,2:]
    return bdata

