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
        StudentID = grades[:, 0]  # returns the first columm in grades
        Name = grades[:, 1]  # returns the second columm in grades
        Assignment1 = grades[:, 2]  # returns the third columm in grades
        Assignment2 = grades[:, 3]  # returns the third columm in grades
        Assignment3 = grades[:, 4]  # returns the third columm in grades
        
    except TypeError:  # if error ocurs, uses indexing for iterables (slower than above, if used on np array)
        grades = grades[1:]
        StudentID, Name, Assignment1, Assignment2, Assignment3 = zip(*grades) 
    
    return StudentID, Name, Assignment1, Assignment2, Assignment3