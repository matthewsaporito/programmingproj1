# -*- coding: utf-8 -*-
"""
Author: Sara Sterlie

"""

import sys
from methods.METHODS import *
import numpy as np




data = None
selection = None
gdata = None
filteredData = None
# Saves variables as None

print("Hello! This is a program for grading students")

data = dataLoad(data)
# Prints velcome-greeting, and loads data trough dataLoad Function.

print("The number of students is {}.".format(len(data.index))) # Prints number of students in the loaded csv-file.
print("The number of assignments is {}.".format(len(list(data.columns-2))-2)) # Prints number of assingments in the loaded csv-file.



while True:
    showMenu() # Displays options in menu trough showMenu function.

    if selection in [1, 2, 3, 4] and data is None:
        print('Please load a CSV-file first.') # Makes sure data is loaded. if not approaching option 2,3 or 4 is not allowed.
        continue
    try:
        selection = int(input("Please enter one of the above options:" ))
        # Asks for selction in menu as user input.

        if selection == 1:
            data = dataLoad()
            print("\nThe number of students in this unfiltered file is {}.\n".format(len(data.index)))
            print(f"\nThe number of assignments is {len(list(data.columns - 2)) - 2}.\n")
        # If user input is 1, scrtipt loads new data through dataLoad function, and prints number of students and assingments in new data-file.
        elif selection == 2:
            filteredData =  filterData(data)
        # If unser input is 2, script displays filtered data through filterData function.
        elif selection == 3:
            mdata = filteredData if filteredData else data
            grades = getGrades(mdata)
            gradesPlot(grades)
        # If user input is 3, script displays plots through gradesPlot function.
        elif selection == 4:
            ndata = filteredData if filteredData else data
            ddata = roundData(ndata)
            grades = getGrades(ndata)
            finalgrade = computeFinalGrade(grades)
            displayGrades(finalgrade, ddata)
        # If user input is 4, script displays the active data through displayGrades function.
        elif selection == 5:
            anykey()
            break
        # If user input is 5, script exits through anykey function
        else:
            print("Invalid Choice. PLease enter one of the above options (1, 2, 3, 4 or 5)!")#prints if user input is different than 1-5

    except ValueError:
       print("please type a number 1-5") # In case of value error script prints except statement.
       continue

