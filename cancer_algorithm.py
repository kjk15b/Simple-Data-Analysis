import csv
import matplotlib.pyplot as plt
import numpy as np

'''
This program abstracts the algorithm used to find values of interest 

from input data files

Carolina Ramirez
MD Anderson

Kolby Kiesling
ACU Nuclear Physics Research Group
'''
'''
def get_Data(ID, *args):
	for x in args:
		
		if ID == "Curtis Positive":
			with open("Curtis_Breast_Detail_1.csv") as csvfile:
                csvReader = csv.reader(csvfile, delimiter=",")
		    	offset = 0
		    	for row in csvReader:
		        	if offset > 1:
		            	if row[22] == "Estrogen Receptor Positive":
		                	x.append(float(row[103]))
		        	offset += 1
		
		elif ID == "Curtis Negative":
			with open("Curtis_Breast_Detail_1.csv") as csvfile:
		    	csvReader = csv.reader(csvfile, delimiter=",")
		    	offset = 0
		    	for row in csvReader:
		        	if offset > 1:
		            	if row[22] == "Estrogen Receptor Negative":
		                	x.append(float(row[103]))
		        	offset += 1		
		
		elif ID == "Curtis Normal":
			with open("Curtis_Breast_Detail_1.csv") as csvfile:
		    	csvReader = csv.reader(csvfile, delimiter=",")
		    	offset = 0
		    	for row in csvReader:
		        	if offset > 1:
			            if row[5] == "Breast" and row[5] != "Breast Carcinoma" and row[5] != "Invasive Breast Carcinoma":
		                	x.append(float(row[103]))
		        	offset += 1
		
		elif ID == "Vande Positive":
			with open("vandeVijver_Breast_Detail.csv") as csvfile:
		    	csvReader = csv.reader(csvfile, delimiter=",")
		    	offset = 0
		    	for row in csvReader:
		        	if offset > 1:
		            	if row[4] == "Estrogen Receptor Positive":
		                	x.append(float(row[32]))   
		        		offset += 1

		elif ID == "Vande Negative":
			with open("vandeVijver_Breast_Detail.csv") as csvfile:
		    	csvReader = csv.reader(csvfile, delimiter=",")
		    	offset = 0
		    	for row in csvReader:
		        	if offset > 1:
		            	if row[4] == "Estrogen Receptor Negative":
		                	x.append(float(row[32]))   
		        		offset += 1

		elif ID == "Gluck Positive":
			with open("Gluck_Breast_Detail.csv") as csvfile:
		    	csvReader = csv.reader(csvfile, delimiter=",")
		    	offset = 0
		    	for row in csvReader:
		        	if offset > 1:
		            	if row[7] == "Estrogen Receptor Positive":
		                	x.append(float(row[28]))   
		        		offset += 1

		elif ID == "Gluck Negative":
			with open("Gluck_Breast_Detail.csv") as csvfile:
		    	csvReader = csv.reader(csvfile, delimiter=",")
		    	offset = 0
		    	for row in csvReader:
		        	if offset > 1:
		            	if row[7] == "Estrogen Receptor Negative":
		                	x.append(float(row[28]))   
		        		offset += 1

		elif ID == "Gluck Normal":
			with open("Gluck_Breast_Detail.csv") as csvfile:
		    	csvReader = csv.reader(csvfile, delimiter=",")
		    	offset = 0
		    	for row in csvReader:
		        	if offset > 1:
			            if row[2] == "Breast" and row[2] != "Breast Carcinoma" and row[2] != "Invasive Breast Carcinoma":
		                	x.append(float(row[28]))   
		        		offset += 1

		elif ID == "Chin Positive":
			with open("Chin_Breast_2_Detail.csv") as csvfile:
		    	csvReader = csv.reader(csvfile, delimiter=",")
		    	offset = 0
		    	for row in csvReader:
		        	if offset > 1:
		            	if row[9] == "Estrogen Receptor Positive":
		                	x.append(float(row[47]))   
		        		offset += 1

		elif ID == "Chin Negative":
			with open("Chin_Breast_2_Detail.csv") as csvfile:
		    	csvReader = csv.reader(csvfile, delimiter=",")
		    	offset = 0
		    	for row in csvReader:
		        	if offset > 1:
		            	if row[9] == "Estrogen Receptor Negative":
		                	x.append(float(row[47]))   
		        		offset += 1



'''
def median_set(*args): # find the median of the set
	for x in args:
		return (len(x) / 2.0)
		
def median_value(i, *args):
	for x in args:
		if i % 1 != 0:
			return ((x[int(i+0.5)] + x[int(i-0.5)]) / 2.0)
		else:
			return x[int(i)]
			
def lower_quartile_find(i, *args):
	for x in args:
		i = float(i / 2.0) # guess that the lower quartile is half of the median
		return median_value(i, x)
		
def upper_quartile_find(i, *args):
	for x in args:
		i = float(i / 2.0) + i
		return median_value(i, x)