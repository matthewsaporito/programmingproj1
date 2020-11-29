# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 14:20:20 2020

@author: apek

"""

import sys
from methods.METHODS import *
import numpy as np

#os.chdir('/Users/Matt/Desktop/')

data = None
selection = None
gdata = None


print("Hello! This is a program for grading student")

#data = filecheck()
data = dataLoad(data)

print("The number of students is {}.".format(len(data.index)))
print("The number of assignments is {}.".format(len(list(data.columns-2))-2))



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
            print(f"\nThe number of assignments is {len(list(data.columns - 2)) - 2}.\n")

        elif selection == 2:
            data = filterData(data)
        elif selection == 3:
            grades = getGrades(data)
            gradesPlot(grades)
        elif selection == 4:
            data = roundData(data)
            grades = getGrades(data)
            finalgrade = computeFinalGrade(grades)
            displayGrades(finalgrade, data)
        elif selection == 5:
            anykey()
            break
        else:
            print("Invalid Choice. PLease enter one of the above options (1, 2, 3, 4 or 5)!")#prints if user input is different than 1-5

    except ValueError:
       print("please type a number 1-5")
       continue

