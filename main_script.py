#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 18:18:05 2020

@author: Sara Sterlie and Anna Pekarova
"""

from methods.dataPlot import *
from methods.dataStatistics import *
from methods.dataLoad import *
from methods.filterData import *
from methods.utils import showMenu
import sys
import numpy as np

    
data = None
active_data = None
active_filter = None


#displays main menu.

while True:
    print(active_filter)
    showMenu()
    
    
    
    selection=int(input("Please enter one of the above options:" )) #asks user for input from utils.

    if selection in [2, 3, 4] and data is None:
        print("Please load data first.")#makes sure data is loaded. if not approaching option 2,3 or 4 is not allowed.
        continue
    
    active_data = active_data if active_data is not None else data
       
    try: 
        if selection == 1:
            data = dataLoad()
            
        elif selection== 2:
            rawdata = data
            active_data, active_filter = filterData(active_data, active_filter)
           
        elif selection == 3:
            print(active_filter)
            statistic = inputStatistics()
            displayStatistic(active_data, statistic)
        
        elif selection == 4:
            dataPlot(active_data)
        
        elif selection == 5:
            sys.exit()
            break
        
        else:
            print("Invalid Choice. PLease enter one of the above options (1, 2, 3, 4 or 5)!")#prints if user input is different than 1-5
            
    except ValueError:
        print("please type a number 1-5")
         
    
  





    

    
    
    

    
    
      
            
    
        
    