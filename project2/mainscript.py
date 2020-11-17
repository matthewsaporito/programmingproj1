#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 15:52:51 2020

@author: sarasterlie
"""

from methods.menu import *
from  methods.filecheck import * 
from methods.gradesPlot import *

data = None
selection = None

choices = ['Load new data', 'Check for data errors', 'Generate plots', 'Display list of grades','Quit program']

while True:
    selection = menu(choices)

    if selection in [2, 3, 4] and data is None:
        print("Please load a CSV-file first.")#makes sure data is loaded. if not approaching option 2,3 or 4 is not allowed.
        continue
    try:
        
        if selection == 1:
            data = loaddata()
        elif selection == 2:
            
        elif selection == 3:
            gradesPlot()
        
        elif selection == 4:
            getColumms()
 
        elif selection == 5:
            any_exit()
#break


#one = "Load new data"
#two = "Check for data errors."
#three =  "Generate plots" 
#four =  "Display list of grades. "
#five = "Quit"

#choices = one, two, three, four, five 

#menu(choices)
