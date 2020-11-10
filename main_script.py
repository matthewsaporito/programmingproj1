#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 18:18:05 2020

@author: sarasterlie and Anna Pekarova
"""

from.dataPlot import *
from.dataStatistics import *
from.dataLoad import *
from.filterData import *


def showMenu():
    print ("1. Load Data")
    print ("2. Filter Data")
    print ("3. Display statistics")
    print ("4. Generate plots")
    print ("5. Quit")
    
    
data = None


showMenu()


while True:
    
    selection=int(input("Please enter one of the above options:" )) 

    if selection in {2, 3, 4} and not data:
        print("Please load data first.")
        showMenu()
        continue
        
        
    try:
        if selection == 1:
            data = dataLoad()
            
        elif selection== 2:
            rawdata = data
            filterData(data)
          
        elif selection == 3:
            statistic = inputStatistics()
            displayStatistic(data, statistic)
            
        elif selection == 4:
            dataPlot(data)
            
        elif selection == 5:
            exit()
            break
        
        else:
            print("Invalid Choice. PLease enter one of the above options (1, 2, 3, 4 or 5)!")
            
    except ValueError:
        print("please type a number 1-5")
         
    
  





    

    
    
    

    
    
      
            
    
        
    