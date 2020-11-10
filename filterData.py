#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:04:32 2020

@author: sarasterlie
"""
import dataLoad
import numpy as np

def filterData(prompt, data):
    
    print("filters:")
    print("1. filter bacteria")
    print("2. filter grwoth rate")
    
    selection =int(input("PLease enter on of the above options:" ))
    

    if selection == 1:
        print("PLease choose a bacteria")
        print("1. Salmonella enterica")
        print("2.Bacillus cereus")
        print("3. Listeria")
        print("4.Brochothrix thermosphacta")

        bacteria = int(input("please choose an option, 1 to 4:"))
    
                while True:
                    bacteria = int(input(prompt))
      
                if bacteria == 1 or bacteria == 2 or bacteria == 3 or bacteria == 4:
                    data = data[ data[:,2]== bacteria,:]
                    return data
                else:
                    print("please enter value 1-4:")
            

             elif selction ==2:
                print("Please specify the range of growthrate")
                lower = float(input("Min growth rate:"))
                upper = float(input("Max growth rate:"))
    
                while True:
                    try:
        
                    lower = float(input("Min growth rate:"))
                    upper = float(input("Max growth rate:"))
                    if lower < upper:
                        data = data[ data[:,1]<upper and data[:,1]>lower,:]
                    break
                except ValueError:
                    print("Please type a number")
 return data 
    
  

 
        
     
      
    
        
        
        
        
    


               
                
            
    
    
 



 
    
