#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 15:52:51 2020

@author: Sara Sterlie
"""




from filecheck import *
from gradesPlot import *
import pandas as pd
import numpy as np
from utils import *

data = None
selection = None
gdata = None

while True:
    print("Hello! This is a program for grading student")

    filecheck(data)
    dataload(gdata)

    print('f{The number of student is:} {len(gdata.index}')
    print('f{The number of asingments are:} {count(gdata.iloc[:,range(2,colnumber)])}')

    choices = ['Load new data', 'Check for data errors', 'Generate plots', 'Display list of grades','Quit program']

    menu(choices)

    data = gdata

    if selection in [1, 2, 3, 4] and data is None:
        print('Please load a CSV-file first.') #Makes sure data is loaded. if not approaching option 2,3 or 4 is not allowed.
        continue

        try:
            selection = menu(choices)
            if selection == 1:
                data = loaddata()
            elif selection == 2:
                filterData(data)
            elif selection == 3:
                gradesPlot()
            elif selection == 4:
                getColumms()
            elif selection == 5:
                
                    sys.exit(0)
            else:
                print("Invalid Choice. PLease enter one of the above options (1, 2, 3, 4 or 5)!")#prints if user input is different than 1-5
            
        except ValueError:
            print("please type a number 1-5")
            continue
