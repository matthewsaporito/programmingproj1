# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 13:44:27 2020

@author: Anna Pekarova
"""

import numpy as np
import statistics as st


def inputNumber(prompt):
    '''
    INPUTNUMBER Prompts user to input a number
    
    Usage: num = inputNumber(prompt) Displays prompt and asks user to input a
    number. Repeats until user inputs a valid number.

    Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
    source: Introduction to programming and data processing with Python Exercises for DTU Course 02631–34, 02691–94. Page 62
    '''
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            pass
    return num
  


DESCRIPTIONS = {
    "Mean Temperature": "Mean (average) Temperature.",
    "Mean Growth rate": "Mean (average) Growth rate.",
    "Std Temperature": "Standard deviation of Temperature.",
    "Std Growth rate": "Standard deviation of Growth rate.",
    "Rows": "The total number of rows in the data.",
    "Mean Cold Growth rate": "Mean (average) Growth rate when Temperature is less than 20 degrees.",
    "Mean Hot Growth rate": "Mean (average) Growth rate when Temperature is greater than 50 degrees.",
}
    
    
def inputStatistics(
        options=np.array([
            "Mean Temperature",
            "Mean Growth rate",
            "Std Temperature",
            "Std Growth rate",
            "Rows",
            "Mean Cold Growth rate",
            "Mean Hot Growth rate",
            "Quit"])
        ):
    '''
    DISPLAYMENU Displays a menu of options, ask the user to choose an item
    and returns the number of the menu item chosen.

    Usage: choice = displayMenu(options)

    Input options Menu options (array of strings)
    Output choice Chosen option (integer)

    Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
    Source: Introduction to programming and data processing with Python Exercises for DTU Course 02631–34, 02691–94. Page 64
    Display menu options
    '''
    
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))
    # Get a valid menu choice
    statistic = 0
    while not(np.any(statistic == np.arange(len(options))+1)):
        statistic = inputNumber("Which statistics would you like to display?")
        
    # if quit
    
    # displayStatistics
        
    return statistic


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

    
    
def displayStatistic(data, statistic):
    print(DESCRIPTIONS[statistic], dataStatistics(data, statistic))
    



  
  
  












