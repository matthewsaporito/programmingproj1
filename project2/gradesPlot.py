# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 15:39:37 2020

@author: Anna Pekarova
"""
import matplotlib.pyplot as plt
from methods.utils import computeFinalGrades
from roundgrade8 import roundGrades
from pandas import NA
from pandas import isnull

def gradesPlot(data, gradesFinal = None ):
    
    gradesFinal = gradesFinal or computeFinalGrades(data)
    
    #  PLOT FINAL GRADES
    #  ------------------------------------------------------------------------
   
    
   
    def histogramData(gradesFinal):   
        ''' 
        I created this function for easier reading, and used some structure I used before: dataPlot from Project 1 made by Anna Pekarova, I also used counter from letter_frequency assignment made by Anna Pekarova
        '''
        counter = {grade: 0 for grade in gradesFinal} # create a counter {grade: zero} for each grade in gradesFinal
    
        for grade in gradesFinal:
            if grade in counter:  # is grade in counter.keys()
                counter[grade] += 1 #if yes add 1 in counter for the key(grade)
    
        grade_counts = sorted(counter.items())  # sorts the counter by the grade
        grades, occurrence = zip(*grade_counts)  # unzips the list of tuples into two lists
        return grades, occurrence
    
    plt.figure(figsize=(9, 9))  # size of the figure
    plt.title('Histogram of grades received by students')  # title of the plot
    plt.xlabel('Grade')  # label of x axis
    plt.ylabel('Number of students')  # label of y axis
    grades, occurrence = histogramData(gradesFinal)  # gets grades and occurrence from histogram_data() 
    plt.bar(grades, occurrence)  # plots the bars
    plt.show() 
    
    
    #  GRADES PER ASSIGNMENT
    #  ------------------------------------------------------------------------
    
    
    def scatterData(data):
         assignmentGrades = [assignments for studentID, name, *assignments in data]
         out1 = []
         for item in assignmentGrades:
             roundedGrades = roundGrades(assignmentGrades)
             out1.append(roundedGrades)
         
         yvals = [item for sublist in out1 for item in sublist]  # used code from: https://stackoverflow.com/a/952952
         outx = []
         
         for sublist in out1:
             x = list(range(1,len(sublist)+1))
             outx.append(x)
             
         xvals = [item for sublist in outx for item in sublist]  # used code from: https://stackoverflow.com/a/952952
         denan = list(zip(xvals,yvals))
         
         out = []
         for xvals,yvals in denan:
            grades = [yval for yval in yvals if isnull(yval) == False]
            out.append([xvals,grades])
         
         x_vals, y_vals = zip(*out)
         return x_vals, y_vals
     
     
     plt.axis([1, max(x_vals), -3, 12])  # sets the range of the x axis to 1 - max number of assignments and of the y axis from -3 to 12
     plt.title('Grades per assignment')  # title
     plt.xlabel('Assignments')  # label of x axis
     plt.ylabel('Grades')  # label of y axis
     
         
    
     
    
             
            
           
            
        
        