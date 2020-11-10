# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 13:44:27 2020

@author: Anna Pekarova
"""

import numpy as np
import statistics as st


def dataStatistics(data, statistic):    
    
    try:  # tries indexing columms as np.array
        temperatures = data[:, 0]  # returns the first columm in data
        growth_rates = data[:, 1]  # returns the second columm in data
        
    except TypeError:  # if error ocurs, uses indexing for iterables 
        temperatures = [item[0] for item in data]  # returns the first columm in data
        growth_rates = [item[1] for item in data]  # returns the second columm in data
    
    if statistic == 'Mean Temperature':  # calculates the average temperature with inbuilt function
        return st.mean(temperatures)
        
    elif statistic == 'Mean Growth rate':  # calculates the average growth rate with inbuilt function
       return st.mean(growth_rates)
       
    elif statistic == 'Std Temperature':  # calculates the standart deviation of temperature
        return st.stdev(temperatures)
        
    elif statistic == 'Std Growth rate':  # calculates the standart deviation of growth
        return st.stdev(growth_rates)
        
    elif statistic == 'Rows':  # returns the lenght of array or iterable
        return len(data)
        
    elif statistic == 'Mean Cold Growth rate':
        # takes growth rate from data if temperature in the same row is < 20 then calculates the average 
        # bacteria is not mentioned because it is not important for this calculation 
        cold_growth_rates = [growth_rate for temperature, growth_rate, _ in data if temperature < 20]
        return st.mean(cold_growth_rates)
        
    elif statistic == 'Mean Hot Growth rate':
        # takes growth rate from data if temperature in the same row is > 50 then calculates the average
        # bacteria is not mentioned because it is not important for this calculation 
        hot_growth_rate = [growth_rate for temperature, growth_rate, _ in data if temperature > 50]
        return st.mean(hot_growth_rate)

    
    
    
    



  
  
  












