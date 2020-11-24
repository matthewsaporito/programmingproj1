#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 15:52:51 2020

@author: Sara Sterlie
"""


#from methods.gradesPlot import *
import pandas as pd
import numpy as np
from methods.data_load import *
from methods.menu import *
from methods.utils import *
from methods.displayGrades import *

os.chdir('/Users/Matt/Desktop/')

data = None
selection = None
gdata = None


print("Hello! This is a program for grading student")

#data = filecheck()
data = dataLoad(data)

print("The number of students is {}.".format(len(data.index)))
#print("The number of assignments is {}.".format({count(data.iloc[:,range(2,colnumber)])}))


#data = gdata

while True:
    showMenu()

    if selection in [1, 2, 3, 4] and data is None:
        print('Please load a CSV-file first.') #Makes sure data is loaded. if not approaching option 2,3 or 4 is not allowed.
        continue
    try:
        selection = int(input("Please enter one of the above options:" ))

        if selection == 1:
            data = dataLoad()
            print("\nThe number of students in this unfiltered file is {}.\n".format(len(data.index)))
        elif selection == 2:
            data = filterData(data)
        elif selection == 3:
            data = roundGrades(data)
            finalGrades = computeFinalGrades(data)
            gradesPlot(data, finalGrades)
        elif selection == 4:
            finalgrade = computeFinalGrades(data)
            data = roundGrades()[1]
            displayGrades(finalgrade, data)
        elif selection == 5:
            anyexit()
        else:
            print("Invalid Choice. PLease enter one of the above options (1, 2, 3, 4 or 5)!")#prints if user input is different than 1-5

    except ValueError:
       print("please type a number 1-5")
       continue

