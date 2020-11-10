#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:04:32 2020

@author: sarasterlie
"""
from .dataLoad import *
from .utils import showMenu
import numpy as np


def filterData(data, active_filter):
        
    if active_filter is not None: 
        print(active_filter)
        
    print("Filters:")
    print("1. Filter bacteria")
    print("2. Filter growth rate")
    print("3. No filter")
    selection =int(input("Please enter on of the above options:" ))#takes user input
    
    while True:
        
        try:
            
            if selection == 1:
                
                    
                print("PLease choose a bacteria")
                print("1 Salmonella enterica")
                print("2 Bacillus cereus")
                print("3 Listeria")
                print("4 Brochothrix thermosphacta")

                bacteria = int(input("please choose an option, 1 to 4:"))#if user input is 1, bacteria-menu is displayed.
                
                ACTIVE_FILTER = {
                    1 : "Salmonella enterica.",
                    2 : "Bacillus cereus.",
                    3 : "Listeria.",
                    4 : "Brochothrix thermosphacta."
                }
        
                if bacteria == 1 or bacteria == 2 or bacteria == 3 or bacteria == 4: #filters for bacteria
                
                    active_filter = ACTIVE_FILTER[bacteria]
                    print("Active Filter: Bacteria :", active_filter)

                    data = data[ data[:,2]== bacteria,:]#overwrites data with new filter for bacteria
                    
                    return data, active_filter
                
                else:           
                    print("Please type a number: 1, 2, 3 or 4")#prints message if user input dosn't fufill requriments.
                     
            
            elif selection == 2:
                print("Please specify the range of growthrate")
                lower = float(input("Min growth rate:"))
                upper = float(input("Max growth rate:"))
                #takes min and max growth rate as input 
                try:
                    data = data[ data[:,1]<upper and data[:,1]>lower,:]#overwrites data with new filter for growthrate
                except ValueError:
                      print("Please enter a number as value for the minimun and maixmun growth rate")#prints message if user input dosn't fufill requriments.
                      
                      active_filter = f"Min. growth rate: {lower} Max.growth rate: {upper}"
                      print("Active Filter: ", active_filter)
                      
                      return data, active_filter
            
            elif selection == 3:
                return None, None
                
        except ValueError:
                print("Please choose an options: 1,2 or 3")#prints message if Valueerror occurs in filter-data menu. 
