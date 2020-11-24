# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 15:39:37 2020

@author: Anna Pekarova
"""
import matplotlib.pyplot as plt
from .utils import computeFinalGrades
from .utils import roundGrades
from pandas import NA
from pandas import isnull
from random import random

def gradesPlot(data, finalGrades):
    
    #  PLOT FINAL GRADES
    #  ------------------------------------------------------------------------
   
    
   
    def histogramData(finalGrades):   
        ''' 
        I created this function for easier reading, and used some structure I used before: dataPlot from Project 1 made by Anna Pekarova, I also used counter from letter_frequency assignment made by Anna Pekarova
        '''
        counter = {grade: 0 for grade in finalGrades} # create a counter {grade: zero} for each grade in gradesFinal
    
        for grade in finalGrades:
            if grade in counter:  # is grade in counter.keys()
                counter[grade] += 1 #if yes add 1 in counter for the key(grade)
    
        grade_counts = sorted(counter.items())  # sorts the counter by the grade
        grades, occurrence = zip(*grade_counts)  # unzips the list of tuples into two lists
        return grades, occurrence
    
    plt.figure(figsize=(9, 9))  # size of the figure
    plt.title('Histogram of grades received by students')  # title of the plot
    plt.xlabel('Grade')  # label of x axis
    plt.ylabel('Number of students')  # label of y axis
    grades, occurrence = histogramData(finalGrades)  # gets grades and occurrence from histogram_data() 
    plt.bar(grades, occurrence)  # plots the bars
    plt.show() 
    
    
    #  GRADES PER ASSIGNMENT
    #  ------------------------------------------------------------------------
    
    
    def scatterData(data):
         assignmentGrades = [assignments for studentID, name, *assignments in data]
         out1 = []
         for item in assignmentGrades:
             roundedGrades = roundGrades(assignmentGrades)[0]
             out1.append(roundedGrades)
         
         yvals = [item for sublist in out1 for item in sublist]  # used code from: https://stackoverflow.com/a/952952
         outx = []
         
         for sublist in out1:
             x = list(range(1,len(sublist)+1))
             outx.append(x)
             
         xvals = [item for sublist in outx for item in sublist]  # used code from: https://stackoverflow.com/a/952952
         denan = list(zip(xvals,yvals))
         denan = [(xval, yval) for xval, yval in denan if isnull(yval) == False]
         
         x_vals, y_vals = zip(*denan)
         return x_vals, y_vals
     
    x_vals,y_vals = scatterData(data) 
    x_vals = [item + 0.1*random()-0.1 for item in x_vals]
    y_vals = [item + 0.1*random()-0.1 for item in y_vals]
    plt.axis([1, max(x_vals), -3, 12])  # sets the range of the x axis to 1 - max number of assignments and of the y axis from -3 to 12
    plt.title('Grades per assignment')  # title
    plt.xlabel('Assignments')  # label of x axis
    plt.ylabel('Grades')  # label of y axis
    plt.scatter(x_vals,y_vals)
    plt.show()
    
        
         
    
     
    
             
            
           
            
        
        