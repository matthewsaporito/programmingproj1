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
        
    if active_filter is not None: #will print variable active_filter when it is assinged 
        print(active_filter)
        
    print("Filters:")
    print("1. Filter bacteria")
    print("2. Filter growth rate")
    print("3. No filter")
    selection =int(input("Please enter on of the above options:" ))
    #filtering menu asks user to choose growthrate of bacteria filter  
    
    while True:
        
        try:
            
            if selection == 1:#if user types 1, programs asks user to choose a bactaria filter. 
                
                    
                print("PLease choose a bacteria")
                print("1 Salmonella enterica")
                print("2 Bacillus cereus")
                print("3 Listeria")
                print("4 Brochothrix thermosphacta")

                bacteria = int(input("please choose an option, 1 to 4:"))#user iput assinged to variable bacteria. 
                
                ACTIVE_FILTER = {#Dictionary translating user input into bacteria names. 
                    1 : "Salmonella enterica.",
                    2 : "Bacillus cereus.",
                    3 : "Listeria.",
                    4 : "Brochothrix thermosphacta."
                }
        
                if bacteria == 1 or bacteria == 2 or bacteria == 3 or bacteria == 4: 
                
                    active_filter = f"Active Filter: Bacteria: {ACTIVE_FILTER[bacteria]}" #assings active_filter variable to description of bacteria filter 
                    print("Active Filter: Bacteria :", active_filter)

                    data = data[ data[:,2]== bacteria,:]#overwrites data with new filter for bacteria.
                    active_data = data
                    return active_data, active_filter
                
                else:           
                    print("Please type a number: 1, 2, 3 or 4")#prints message if user input dosn't fufill requriments.
                     
            
            elif selection == 2:
                print("Please specify the range of growthrate")
                lower = float(input("Min growth rate:"))
                upper = float(input("Max growth rate:"))
                #takes min and max growth rate as input 
                try:
                    data = data[ data[:,1] < upper]
                    data = data[ data[:,1] > lower]#overwrites data with new filter for growthrate
                except ValueError:
                      print("ERROR: Please enter a number as value for the minimun and maixmun growth rate")#prints message if user input dosn't fufill requriments.
            
            elif selection == 3:
                return None, None
            
            active_filter = f"Min. growth rate: {lower} Max.growth rate: {upper}" #assings active_filter variable, to describtion of min and max growthrate. 
            print("Active Filter: ", active_filter)
            active_data = data
            return active_data, active_filter
                
        except ValueError:
                print("Please choose an options: 1,2 or 3")#prints message if Valueerror occurs in filter-data menu. 
