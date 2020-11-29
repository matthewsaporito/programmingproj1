# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 14:11:09 2020

@author: apek
"""

import os
import numpy as np
import pandas as pd
import math as m
from pandas import NA
from copy import copy
from pandas import isnull
import matplotlib.pyplot as plt
from random import random



# Menu options presented to user
def showMenu():
    """
    Author: Sara Sterlie
    """  
    print("1. Load new data.")
    print("2. Check for data errors.")
    print("3. Generate plots")
    print("4. Display list of grades.")
    print("5. Quit")


def filecheck():
    #checks that user file exists loads as 'data'
    filename = str(input("Please enter The file you wish to load:"))
    
    try:
        # data = np.loadtxt(filename, delimiter=" ")
        data = pd.DataFrame([line.strip().split(',') for line in open(filename, 'r')]) #converts csv file to pandas dataframe
        return data[1:]#returns data excluding headers
    except OSError:
        print("The file could not be found. Please Enter an existing file")
        return filecheck()
    except Exception as e:
        print(e)
        return filecheck()


def dataLoad(gdata=None): #converts columns 2 onward to numeric for use in claculations
    gdata = filecheck()
    lll=list(gdata.columns) #gets list of column numbers
    gdata[lll[2:]] = pd.to_numeric(gdata[lll[2:]].stack(), errors='coerce').unstack()#data formatting from https://stackoverflow.com/questions/36814100/pandas-to-numeric-for-multiple-columns
    return gdata


def filterData(gdata, log=True):
    try:
        dfcol1 = pd.DataFrame(gdata, columns=[0])
    except ValueError:
        gdata = pd.DataFrame.from_records(gdata)
        dfcol1 = pd.DataFrame(gdata, columns=[0])

    print(dfcol1)
    duplicaterow = dfcol1[dfcol1.duplicated()]
    if log:  # will only print error rows in a later module if log is true
        print(
            "\nThe following rows contain duplicate student IDs, the row with the first duplicate occurence will be kept:\n",
            "\n", duplicaterow.to_string(header=False))
    data = gdata[gdata[0].notnull()].drop_duplicates(subset=0,
                                                     keep='first')  # pandas code from https://stackoverflow.com/questions/45655080/remove-duplicates-using-pandas-python

    print("\n The data has been filtered, now the number of students is {}.\n".format(len(data.index)))

    if log:  # will only print error rows in a later module if log is true
        colnumber = len(list(gdata.columns))
        datacols = gdata.iloc[:, range(2,
                                       colnumber)]  # https://python-forum.io/Thread-Iterating-over-pandas-df-to-check-for-values-out-of-range?page=2
        rownumber = len(gdata.index)

        rownum = 0
        for rownumber in datacols.values:
            for i in rownumber:
                if (i < -3 or i > 12):
                    print("We found a grade outside range at row number {}, the grade is {}.".format(rownum + 2, i))
            rownum += 1

    data = data.values.tolist()
    return data


def roundGrades(grades):
    out = grades
    
    for k, i in enumerate(grades):
        if pd.isnull(i) == True:
            out[k] = NA
        elif (i <= 12 and i >= 11):
            out[k] = 12
        elif (i < 11 and i >= 8.5):
            out[k] = 10
        elif (i < 8.5 and i >= 5.5):
            out[k] = 7
        elif (i < 5.5 and i >= 3):
            out[k] = 4
        elif (i < 3 and i >= 1):
            out[k] = 2
        elif (i < 1 and i >= -1.5):
            out[k] = 0
        elif (i <-1.5 and i >= -3):
            out[k] = -3
        else:
            out[k] = NA
            
    gradesRounded = out
    return gradesRounded
    
def roundData(data):
    data = filterData(data, log = False)
    
    for g, (studentID, name, *grades) in enumerate(data):
        data[g] = [studentID, name, *roundGrades(grades)]
        
    data = np.array(data)
    return data


def getGrades(data):
     """
     Author: Anna Pekarove
     use: gets An N ×M matrix containing grades on the 7-step-scale given to N students on M different assignments from data.
     """
     try:  # tries to change data to list if data is in pandas format
         data2 = data.values.tolist() 
     except:  # if thar does not work, tries to change data to  list the np.array method
         data2 = list([list(item) for item in data])
        
    
     out = []  # creates an empty list
     for name,studentID, *assignments in data2:  # for name, studentId, *assignments in data2
         roundedGrades = roundGrades([*assignments])  # finds rounded grades from assignments calling the function roundGrades
         out.append(roundedGrades)  # puts the values into the empty list 
     grades = np.array(out)  # changes the list into a np.array
     return grades 
    


def computeFinalGrades(grades):
    """
    Computes final grades
    Parameters:
        data: iterable that contains (studentID, name, assignment1, ..., assignmentN)
    Return: 
        np.array of final grades
    Author: Anna Pekarova
    """
    
    assignmentGrades = list(list(grade) for grade in grades) # creates a list from np.array
    out1 = []  # creates an empty list
    for item in assignmentGrades:  # for each list in list of list
        
        Grades = [grade for grade in item if isnull(grade) == False]  # get rid of nans
        out1.append(Grades)  # adds the values to the list
    
    out = []  # creates a new empty list
    for item in out1:  # for each list in the list out1
       if -3 in item:  # if there is -3 in the list in the list
           finalGrade = -3  # then the final grade is -3
           
       else:
           
           sortedList = sorted(item)  # sorts the numbers in the list in the list from the smallest up
           
           if len(sortedList) > 1:  
               sortedList = sortedList[1:]  # cuts of the smallest one
           numberOfAssignments = len(sortedList)  # gets the lenght of of a list in the list
           finalGrade = sum(sortedList)/numberOfAssignments  # gets the final grade for each student
    
       out.append(finalGrade)  #saves a grade into the empty list
       
    roundedOut =  roundGrades(out)  # rounds the grades
    
    gradesFinal = np.array(roundedOut)  # crreates an np.array out of the list
    return gradesFinal


"""
Created on Tue Nov 24 13:11:15 2020

@author: Matt Saporito
"""


#merge calculated finale grade with the rest of grade data to display

def displayGrades(finalgrade, data):
    finalgrade = pd.DataFrame(finalgrade)

    finalgrade.columns=['Final Grade']

    db = pd.DataFrame(data)
    db.columns=['student ID', 'Name', *['Assignment ' + str(x) for x in range(1, len(data[0]) - 1)]]
    df = pd.concat([db, finalgrade], axis=1)  # concatenates calculates grades and input data
    print(df.sort_values(['Name']))
    return df.sort_values(['Name'])
    
def gradesPlot(grades):
    """
    Author: Anna Pekarova
    """
    
    finalGrades1 = computeFinalGrades(grades)  # computes final grades with computeFinalGrades function
    finalGrades = list(finalGrades1)  # makes list from np.array
    grades1 = list([list(item) for item in grades])  # transform np.array of grades to list of lists
    
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
    plt.xticks([-3,0,2,4,7,10,12])  #  plots ticks on x axis
    grades, occurrence = histogramData(finalGrades)  # gets grades and occurrence from histogram_data() 
    plt.bar(grades, occurrence)  # plots the bars
    plt.show() 
    
    
    #  GRADES PER ASSIGNMENT
    #  ------------------------------------------------------------------------
    
    
    def scatterData(grades1):
         assignmentGrades = grades1  # gets list of lists of grades = gets rid of studentIDs and names
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
     
    x_vals,y_vals, x_values, y_values = scatterData(grades1)  # calls the above function to get x and y valus
    x_vals = [item + 0.1*random()-0.1 for item in x_vals]  # adds a random number between -0.1 and 0.1 to each x value
    y_vals = [item + 0.1*random()-0.1 for item in y_vals]  # adds a random number between -0.1 and 0.1 to each y value
    plt.axis([0, max(x_vals) + 1, -4, 13])  # sets the range of the x axis to 0 - max number of assignments + 1 and of the y axis from -4 to 13, I do so so that the plot is visible better
    plt.title('Grades per assignment')  # title
    plt.xlabel('Assignments')  # label of x axis
    plt.ylabel('Grades')  # label of y axis
    plt.yticks([-3,0,2,4,7,10,12])  # adds
    plt.scatter(x_vals,y_vals)  # plots the values as a scatter
    plt.plot(x_values, y_values)
    plt.show()