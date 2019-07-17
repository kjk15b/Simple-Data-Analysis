#!/bin/python

'''
-------------------------------------------
Carolina Ramirez
M.D. Anderson
-------------------------------------------
Kolby Kiesling
ACU Nuclear Physics Research Group
-------------------------------------------
This program generates a random set of data 
and presents a box & whisker plot of that 
data
-------------------------------------------
'''

import matplotlib.pyplot as plt
import numpy as np

# first step, we need to make a 'box' of random data to fill
junk_data = list() # make an empty list called junk_data we will fill it later with good data
N_junk_data = list()

print "\nHow many data points do you want to include? "
num_points = int(input()) # read input on the number of points to analyze

for i in range(num_points): # start a loop to make random data and fill our 'box' starts at 0 -> user input (num_points)
    junk_data.append(np.random.rand(1) * 10) # add a random data point to our 'box' that can range from 0 -> 10
    N_junk_data.append(0)

print junk_data # print out the contents of the data we created

# now we want to sort the data to easily figure out where medians are
junk_data.sort() # this sorts the 'box' from 0 -> 10

'''
Now here is where we get into some simple data analysis and algorithmic searching
Fun stuff, but you should get the hang of it with how to find points of interest in unknown data sets
'''

# -------------------------------------------
# Tons of variable declarations
# -------------------------------------------
hl_value = 0 # declaration of variables necessary to find the median of the data set, 
hf_value = 0 # hl and hf are in the case that the median index is not a whole number

uneven_flag = False # set the flag to false initially, e.g. we assume our data sets are even, median = 1.0, 2.0... 10.0 whole numbers
median_data = 0 # a variable to store what the median of our data set is

# -------------------------------------------
# Because in nuances in numpy, we will save all of our data in a list
maximum_data = [0] # lists with only one item, one dimensional boxes
minimum_data = [0] 
median_total = [0]
lower_median = [0]
upper_median = [0]
# --------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------
# FINDING THE FIRST OVERALL MEDIAN
# --------------------------------------------------------------------------------------

# The first thing we want to do is to find the median of the data set, to find that we can simply find the length of our 'box'

length = len(junk_data) # the length, or number of data points in our set is saved now in the length variable

# Now we are concerned with finding the index at which the median is at in our 'box', where it is located

median_index = float((length + 1) / 2) # Add one to length because our box is zero indexed then divide by two to find the midpoint essentially


if median_index % 1 != 0: # if our median index has 0.5 attached to it do as follows, e.g. 6.5
    hl_value = median_index - 0.5 # step down by 1/2
    hf_value = median_index + 0.5 # step up by 1/2
    uneven_flag = True # set the flag for true for later analysis
    
# Now we have found our index for the median and now it is time to find the actual value of it
if uneven_flag: # if the uneven flag is raised do as follows
            median_total[0] = (junk_data[hl_data] + junk_data[hf_value]) / 2 # take the average of the two points around the median

else: # otherwise if the flag is not raised, continue as follows
    median_index = int(median_index)
    median_total[0] = junk_data[median_index]# if the median index was a whole number then the median is that value
    
uneven_flag = False # reset the flag

# --------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------
    
    
# --------------------------------------------------------------------------------------    
# FINDING THE LOWER MEDIAN
# --------------------------------------------------------------------------------------    
# To find our lower median we know to search one less than where our total median is
low_index = float(median_index / 2)

if low_index % 1 != 0:
    hl_value = lower_median[0] - 0.5 # step down by 1/2
    hf_value = lower_median[0] + 0.5 # step up by 1/2
    uneven_flag = True # set the flag for true for later analysis
    
# Now we have found our index for the median and now it is time to find the actual value of it
if uneven_flag: # if the uneven flag is raised do as follows
            lower_median[0] = (junk_data[hl_data] + junk_data[hf_value]) / 2 # take the average of the two points around the median

else: # otherwise if the flag is not raised, continue as follows
    lower_median[0] = junk_data[int(low_index)] # if the median index was a whole number then the median is that value

uneven_flag = False # reset the flag
    
# --------------------------------------------------------------------------------------    
# FINDING THE UPPER MEDIAN
# --------------------------------------------------------------------------------------    
# To find our lower median we know to search one less than where our total median is
upper_index = float((median_index / 2) + median_index)

if upper_index % 1 != 0:
    hl_value = lower_median[0] - 0.5 # step down by 1/2
    hf_value = lower_median[0] + 0.5 # step up by 1/2
    uneven_flag = True # set the flag for true for later analysis
    
# Now we have found our index for the median and now it is time to find the actual value of it
if uneven_flag: # if the uneven flag is raised do as follows
            upper_median[0] = (junk_data[hl_data] + junk_data[hf_value]) / 2 # take the average of the two points around the median

else: # otherwise if the flag is not raised, continue as follows
    upper_median[0] = junk_data[int(upper_index)] # if the median index was a whole number then the median is that value    
    
# --------------------------------------------------------------------------------------    
# FINDING MAX AND MIN VALUES
# --------------------------------------------------------------------------------------    
# To find our lower median we will utilize the functions .max() and .min()
maximum_data[0] = max(junk_data) # this saves the largest value in junk to this 'box'
minimum_data[0] = min(junk_data) # this saves the smallest value in junk to this 'box'

# --------------------------------------------------------------------------------------    
# NORMALIZATION
# --------------------------------------------------------------------------------------  
# Not really necessary, but a unique approach to be able to modify large quantities of data at one
# Here I will normalize everything with respect to the median_total or the center
# This will produce a graph that will show how closely each data point is related to the center or median
N_maximum_data = [0] # lists with only one item, one dimensional boxes
N_minimum_data = [0]  # The N is for normalized
N_median_total = [0]
N_lower_median = [0]
N_upper_median = [0]
# -------------------------------------------
# Because in nuances in numpy, we will save all of our data in a list
N_maximum_data[0] = maximum_data[0] / median_total[0] # lists with only one item, one dimensional boxes
N_minimum_data[0] = minimum_data[0] / median_total[0]  # The N is for normalized
N_median_total[0] = median_total[0] / median_total[0]
N_lower_median[0] = lower_median[0] / median_total[0]
N_upper_median[0] = upper_median[0] / median_total[0]

N_junk_data = list(map(lambda x : x / median_total[0], junk_data)) # normalize junk data
# --------------------------------------------------------------------------------------
# I did not realize that I had already reduced and extracted all I needed from the data,
# I thought I was going to need the lambda function, but oh well, for big data we can use that
# --------------------------------------------------------------------------------------    
# PLOTTING
# -------------------------------------------------------------------------------------- 
# Generating the two subsequent plots, raw data and normalized

data = np.concatenate((junk_data, median_total, upper_median, lower_median))
N_data = np.concatenate((N_junk_data, N_median_total, N_upper_median, N_lower_median))

plt.figure(1)
fig1, ax1 = plt.subplots()
plt.title('Raw Data')
plt.ylabel('Measured Value ( )')
ax1.boxplot(data)

plt.figure(2)
fig2, ax2 = plt.subplots()
plt.title("Normalized Data")
plt.ylabel("Normalized Measurements ( )")
ax2.boxplot(N_data)

plt.show()