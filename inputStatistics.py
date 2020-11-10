# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 11:32:48 2020

@author: Anna Pekarova
"""

import numpy as np



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


def displayStatistic(data, statistic)
    print(DESCRIPTIONS[statistic], dataStatistics(data, statistics))
