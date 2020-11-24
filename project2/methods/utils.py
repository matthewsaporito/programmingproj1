# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:04:34 2020

@author: apek
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 19:22:30 2020

@author: Anna Pekarova
"""

import numpy as np
import math as m
from pandas import isnull
from pandas import NA
import pandas as pd
from pandas import isnull
from .data_load import filterData



def menu(choices):
    
    for i, choice in enumerate(choices):
        print(f"{i+1}.: {choice}")
    
    while True:
        
        selection=int(input("Please enter one of the above options:" )) 
            
        if selection in range(1, len(choices)):
            return choices[selection]
        else:
            print("Invalid Choice. Please choose one out of", range(1, len(choices)))
            
def roundGrades():
    
    data = filterData(log=False)

    for g, (studentID, name, *grades) in enumerate(data):
        for k, i in enumerate(grades):
            if (i <= 12 and i >= 11):
                data[g][k + 2] = 12
            elif (i < 11 and i >= 8.5):
                data[g][k + 2] = 10
            elif (i < 8.5 and i >= 5.5):
                data[g][k + 2] = 7
            elif (i < 5.5 and i >= 3):
                data[g][k + 2] = 4
            elif (i < 3 and i >= 1):
                data[g][k + 2] = 2
            elif (i < 1 and i >= -1.5):
                data[g][k + 2] = 0
            elif (i <-1.5 and i >= -3):
                data[g][k + 2] = -3
            else:
                data[g][k + 2] = NA
                
            data = np.array(data)   
            bdata = data[:,2:]
            bdata = bdata.tolist()
    return bdata, data


def computeFinalGrades(data):
    """
    Computes final grades
    Parameters:
        data: iterable that contains (studentID, name, assignment1, ..., assignmentN)
    Return: 
        np.array of final grades
    Author: Anna Pekarova
    """
    assignmentGrades = [assignments for studentID, name, *assignments in data]  # gets list of lists of assignment grades
    
    out1 = []  # creates an empty list
    
    for item in assignmentGrades:  # for each list in list of list
       Grades1 = [grade for grade in item if isnull(grade) == False]  # get rid of nans
       Grades = roundGrades(Grades1)[0]  # calls the round function for each row
       out1.append(Grades)  # adds the values to the list
    
    out = []  # creates a new empty list
    for item in out1:  # for each list in the list out1
       if -3 in item:  # if there is -3 in the list in the list
           finalGrade = -3  # then the final grade is -3

       else:
           sortedList = sorted(item)  # sorts the numbers in the list in the list from the smallest up
           trimmedList = sortedList[1:]  # cuts of the smallest one
           numberOfAssignments = len(trimmedList)  # gets the lenght of of a list in the list
           finalGrade = sum(trimmedList)/numberOfAssignments  # gets the final grade for each student
         
       out.append(finalGrade) # adds this grade to the empty list
   
    gradesFinal = np.array(out)  # changes the list into a numpy array
    return gradesFinal
    
    
    

