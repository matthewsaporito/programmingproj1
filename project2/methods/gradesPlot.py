# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 15:39:37 2020

@author: Anna Pekarova
"""
import matplotlib.pyplot as plt
from pandas import NA
from pandas import isnull
from random import random
import numpy as np


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
    plt.title('Histogram of final grades received by students')  # title of the plot
    plt.xlabel('Grade')  # label of x axis
    plt.ylabel('Number of students')  # label of y axis
    plt.xticks([-3,0,2,4,7,10,12])
    grades, occurrence = histogramData(finalGrades)  # gets grades and occurrence from histogram_data() 
    plt.bar(grades, occurrence)  # plots the bars
    plt.show() 
    
    
    #  GRADES PER ASSIGNMENT
    #  ------------------------------------------------------------------------
    
    
    def scatterData(data):
         assignmentGrades = [assignments for studentID, name, *assignments in data]  # gets list of lists of grades = gets rid of studentIDs and names
         
         yvals = [item for sublist in assignmentGrades for item in sublist]  # used code from: https://stackoverflow.com/a/952952, from a list of lists makes just a list
         outx = []  # cretes an empty list
         
         for sublist in assignmentGrades:  # for a list in the list of lists named assignmentGrades
             x = list(range(1,len(sublist)+1))  # cretes a list filled with indexes + 1 of values in list, corresponds to number of assignments
             outx.append(x)  # saves these lists into the empty list
             
         xvals = [item for sublist in outx for item in sublist]  # used code from: https://stackoverflow.com/a/952952, from a list of lists makes just a list
         vals = list(zip(xvals,yvals))  # makes list of tuples consisting of x and y values
         vals = [(xval, yval) for xval, yval in vals if isnull(yval) == False]  # deletes a tuple from the list if there is NA in the tuple
         
         
         dictionary = {xval: [] for xval, yval in vals}   # creates
         for xval, yval in vals:
             dictionary[xval].append(yval)
        
         dictionaryAvg = {key: sum(value)/len(value) for key, value in dictionary.items()} 
         x_values, y_values = zip(*dictionaryAvg.items())    
        
         x_vals, y_vals = zip(*vals)  # uzips the list of tuples into two lists
         
         return x_vals, y_vals, x_values, y_values
     
    x_vals,y_vals, x_values, y_values = scatterData(data)  # calls the above function to get x and y valus
    x_vals = [item + 0.1*random()-0.1 for item in x_vals]  # adds a random number between -0.1 and 0.1 to each x value
    y_vals = [item + 0.1*random()-0.1 for item in y_vals]  # adds a random number between -0.1 and 0.1 to each y value
    plt.axis([1, max(x_vals), -3, 12])  # sets the range of the x axis to 1 - max number of assignments and of the y axis from -3 to 12
    plt.title('Grades per assignment')  # title
    plt.xlabel('Assignments')  # label of x axis
    plt.ylabel('Grades')  # label of y axis
    plt.scatter(x_vals,y_vals)  # plots the values as a scatter
    plt.plot(x_values, y_values)
    plt.show()
    
        
         
    
     
    
             
            
           
            
        
        