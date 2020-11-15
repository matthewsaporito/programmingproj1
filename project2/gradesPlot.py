# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 15:39:37 2020

@author: Anna Pekarova
"""
import matplotlib.pyplot as plt
from methods.utils import computeFinalGrades

def gradesPlot(grades):
    gradesFinal = gradesFinal if gradesFinal is not None else computeFinalGrades(grades)
    
    #  PLOT FINAL GRADES
    #  ------------------------------------------------------------------------
   
    def histogram_data(gradesFinal):   
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
    grades, occurrence = histogram_data(gradesFinal)  # gets grades and occurrence from histogram_data() 
    plt.bar(grades, occurrence)  # plots the bars
    plt.show() 
    
    
    #  GRADES PER ASSIGNMENT
    #  ------------------------------------------------------------------------