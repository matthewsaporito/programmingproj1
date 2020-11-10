#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:04:32 2020

@author: sarasterlie
"""
from .dataLoad import *
from .utils import *
import numpy as np


def filterData(prompt, data):
    print("Filters:")
    print("1. Filter bacteria")
    print("2. Filter grwoth rate")
    print("3. Return to main menu")
        
    while True:
        
        selection =int(input("Please enter on of the above options:" ))

        try:
            
            if selection == 1:
                
                print("PLease choose a bacteria")
                print("1. Salmonella enterica")
                print("2.Bacillus cereus")
                print("3. Listeria")
                print("4.Brochothrix thermosphacta")

                bacteria = int(input("please choose an option, 1 to 4:"))
    
            
                if bacteria == 1 or bacteria == 2 or bacteria == 3 or bacteria == 4:
                
                    data = data[ data[:,2]== bacteria,:]
                else:
                    print("Please type a number: 1, 2, 3 or 4")  
                    
                    return data  
            
    
            elif selection == 2:
                print("Please specify the range of growthrate")
                lower = float(input("Min growth rate:"))
                upper = float(input("Max growth rate:"))
                try:
                    data = data[ data[:,1]<upper and data[:,1]>lower,:]
                except ValueError:
                      print("Please enter a number as value for the minimun and maixmun growth rate")
                      
                      return data 
                
    
            elif selection == 3:
                
                showMenu()
                
        except ValueError:
                print("Please choose an options: 1,2 or 3")
    
  

 
        
     
      
    
        
        
        
        
    


               
                
            
    
    
 



 
    
