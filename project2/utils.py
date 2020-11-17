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



def menu(choices):
    
    for i, choice in enumerate(choices):
        print(f"{i+1}.: {choice}")
    
    while True:
        
        selection=int(input("Please enter one of the above options:" )) 
            
        if selection in range(1, len(choices)):
            return choices[selection]
        else:
            print("Invalid Choice. Please choose one out of", range(1, len(choices)))
            

def getColumms(grades):
    grades = sorted(grades, key = lambda grades_entry: grades_entry[0])  # sorts the grades by the first columm 
    studentIDs, names, assignments1, assignments2, assignments3 = zip(*grades)
    return studentIDs, names, assignments1, assignments2, assignments3


def computeFinalGrades(grades): 
   assignmentGrades = [[assignments1, assignments2, assignments3] for studentIDs, names, assignments1, assignments2, assignments3 in grades]  # gets list of lists of assignment grades
   out = []  # creates an empty list
   
   for item in assignmentGrades:  # for each list in list of list
       numberOfAssignments = len([grade for grade in item if grade])  # gets the lenght of of a list in list of lists not counting Nones
       finalGrade = sum(assignmentGrades)/numberOfAssignments  # gets the final grade for each student
       out.append(finalGrade)  # saves the final grade into the empty list
   
   gradesFinal = np.array(out)  # changes empty list into a numpy array (I prefer to work with iterables
   return gradesFinal