# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:00:08 2020

@author: Anna Pekarova
"""


import matplotlib.pyplot as plt



def dataPlot(data):

    try:  # tries indexing columms as np.array (preffered)
        temperatures = data[:, 0]  # returns the first columm in data
        growth_rates = data[:, 1]  # returns the second columm in data
        bacteria_ids = data[:, 2]  # returns the third columm in data
        
    except TypeError:  # if error ocurs, uses indexing for iterables (slower than above, if used on np array)
        temperatures, growth_rates, bacteria_ids = zip(*data) 
       
    bacteria_dictionary = {  # dictionary which says for what bacteria should each number be exchanged
        1 : 'Salmonella enterica',   
        2 : 'Bacillus cereus',
        3 : 'Listeria',
        4 : 'Brochothrix thermosphacta'
    }
    
     #  NUMBER OF BACTERIA
     #  -------------------------------------------------------
     
    def histogram_data(bacteria_ids):
        '''creates a function for easier reading'''
        
        counter = {i: 0 for i in range(1, 5)}  # creates a counter, with keys of i = {1, 2, 3, 4} and assigned values 0
        
        for bacteria_id in bacteria_ids:  
            counter[bacteria_id] = counter[bacteria_id] + 1 if bacteria_id in counter else 1  # increments 1 in counter[bacteria_id] if number in counter, else assigns 1
            
        bacteria_counts = sorted(counter.items())  # sorts the counter by bacteria_id
        bacteria_counts = [(bacteria_dictionary[bacteria_id], count) for bacteria_id, count in bacteria_counts]  # for every bacteria_id and its count in bacteria_counts creates a tuple with name of the bacteria and the count
            
        names, values = zip(*bacteria_counts)  # unzips the list of tuples into two lists
        return names, values
    
    plt.figure(figsize=(9, 9))  # size of the figure
    plt.title('Histogram of Number of bacteria')  # title of the plot
    plt.xlabel('Type of bacteria')  # label of x axis
    plt.ylabel('Number of bacteria')  # label of y axis
    names, values = histogram_data(bacteria_ids)  # gets names and values from histogram_data() 
    plt.bar(names, values)  # plots the bars
    plt.show() 
    
    #  GROWTH RATE BY TEMPERATURE  
    #  -------------------------------------------------------
    
    def growth_data(data):
        '''function for easier reading'''
        bacteria_development = {  # dictionary of dictionaries, every bacteria id has a dictionary of temperatures and growth rates assigned
            n: [(temperature, growth_rate) for temperature, growth_rate, bacteria in data if bacteria == n] for n in {1, 2, 3, 4}
        } 
        
        out = []  # empty list

        for n, bacteria_data in bacteria_development.items():  # for every n and its bacteria_data in bacteria_development dictionary
            x_vals, y_vals = zip(*bacteria_data)  # creates a tuple of x and y values by unzipping bacteria_data
            name = bacteria_dictionary[n]  # also assigns a name for n from bacteria_dictionary
            out.append((x_vals, y_vals, name))  # puts the values into the empty list
        
        return out
    
    plt.axis([10, 60, 0, max(growth_rates) * 1.5])  # sets the range of the x axis to 10 - 60 and of the y axis from 0 to the max value of growth rate * 1.5, so there is space for the legend
    plt.title('Growth rate by temperature')  # title
    plt.xlabel('Temperature')  # label of x axis
    plt.ylabel('Growth rate')  # label of y axis
    for x_vals, y_vals, name in growth_data(data):  # get x, y values and name from the growth_data function 
        plt.plot(x_vals, y_vals, label = name)  # plots these x, y values and uses the name as a label of the plot
    plt.legend(loc="best")  # places the legend at the best spot
    plt.show()
    
    



