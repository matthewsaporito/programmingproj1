#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 18:18:05 2020

@author: sarasterlie and Anna Pekarova
"""

from methods.dataPlot import *
from methods.dataStatistics import *
from methods.dataLoad import *
from methods.filterData import *
from methods.utils import showMenu
import numpy as np

    
data = None
filtered_data = None



#displays main menu.

while True:
    showMenu()
    selection=int(input("Please enter one of the above options:" )) #asks user for input from utils.

    if selection in [2, 3, 4] and data is None:
        print("Please load data first.")#makes sure data is loaded. if not approaching option 2,3 or 4 is not allowed.
        showMenu()
        continue
    
    active_data = filtered_data or data 
       
    try: 
        if selection == 1:
            data = dataLoad()
            
        elif selection== 2:
            rawdata = data
            filtered_data = filterData(data)
          
        elif selection == 3:
            statistic = inputStatistics()
            displayStatistic(active_data, statistic)
            
        elif selection == 4:
            dataPlot(active_data)
            
        elif selection == 5:
            exit()
            break
        
        else:
            print("Invalid Choice. PLease enter one of the above options (1, 2, 3, 4 or 5)!")#prints if user input is different than 1-5
            
    except ValueError:
        print("please type a number 1-5")
         
    
  





    

    
    
    

    
    
      
            
    
        
    