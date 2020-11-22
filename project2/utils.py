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



def menu(choices):
    
    for i, choice in enumerate(choices):
        print(f"{i+1}.: {choice}")
    
    while True:
        
        selection=int(input("Please enter one of the above options:" )) 
            
        if selection in range(1, len(choices)):
            return choices[selection]
        else:
            print("Invalid Choice. Please choose one out of", range(1, len(choices)))
            
'''
def getColumms(filteredData):
    filteredData = sorted(filteredData, key = lambda filteredData_entry: filteredData_entry[0])  # sorts the grades by the first columm 
    studentIDs, names, *args = zip(*filteredData)
    return studentIDs, names, *args
'''


def computeFinalGrades(data): 
   assignmentGrades = [assignments for studentID, name, *assignments in data]  # gets list of lists of assignment grades
   out1 = []  # creates an empty list
   
   for item in assignmentGrades:  # for each list in list of list
       Grades = [grade for grade in item if isnull(grade) == False]  # get rid of nans
       out1.append(Grades)
      
   out = []
   for it in out:
       numberOfAssignments = len([it])  # gets the lenght of of a list in list of lists not counting Nones
       finalGrade = sum(it)/numberOfAssignments  # gets the final grade for each student
       out.append(finalGrade)  # saves the final grade into the empty list
   
   gradesFinal = np.array(out)  # changes empty list into a numpy array (I prefer to work with iterables
   return gradesFinal

