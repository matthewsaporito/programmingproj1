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
    try:  # tries indexing columms as np.array (preffered)
        grades = np.delete(grades, (0), axis=0)   # deletes the first row
        studentIDs = grades[:, 0]  # returns the first columm in grades
        names = grades[:, 1]  # returns the second columm in grades
        assignments1 = grades[:, 2]  # returns the third columm in grades
        assignments2 = grades[:, 3]  # returns the third columm in grades
        assignments3 = grades[:, 4]  # returns the third columm in grades
        
    except TypeError:  # if error ocurs, uses indexing for iterables (slower than above, if used on np array)
        grades = grades[1:]
        studentIDs, names, assignments1, assignments2, assignments3 = zip(*grades) 
    
    return studentIDs, names, assignments1, assignments2, assignments3


def computeFinalGrades(grades):
   try:
       grades = np.delete(grades, (0), axis=0)  # tries indexing columms as np.array (preffered), this is also used in the getColumms function
   except TypeError:  # if error ocurs, uses indexing for iterables (slower than above, if used on np array)
        grades = grades[1:]
    
   assignmentGrades = [[assignments1, assignments2, assignments3] for studentIDs, names, assignments1, assignments2, assignments3 in grades]  # gets list of lists of assignment grades
   gradesFinal = []  # creates an empty list
   
   for item in assignmentGrades:  # for each list in list of list
       numberOfAssignments = len([grade for grade in item if grade])  # gets the lenght of of a list in list of lists not counting Nones
       finalGrade = sum(assignmentGrades)/numberOfAssignments  # gets the final grade for each student
       gradesFinal.append(finalGrade)  # saves the final grade into the empty list
        
   return gradesFinal