#!/bin/python

# -------
# Test program for R / W

import csv
import matplotlib.pyplot as plt
import numpy as np
import cancer_algorithm as ca

# ------------
# Defining some global variables
# ------------
curtis_pos_NDUT = list() # positive estrogen receptor counts
curtis_neg_NDUT = list() # negative estrogen receptor counts
curtis_nor_NDUT = list() # normal background
# -----------
# VandeVijver
# ----------
vande_pos_NDUT = list() # positive estrogen receptor counts
vande_neg_NDUT = list() # negative estrogen receptor counts
vande_nor_NDUT = list() # normal background
# ----------
# Gluck
# ----------
gluck_pos_NDUT = list() # positive estrogen receptor counts
gluck_neg_NDUT = list() # negative estrogen receptor counts
gluck_nor_NDUT = list() # normal background
# ----------
# Chin
# ----------
chin_pos_NDUT = list() # positive estrogen receptor counts
chin_neg_NDUT = list() # negative estrogen receptor counts
chin_nor_NDUT = list() # normal background
# ---------
# TCGA
# ---------
tcga_pos_NDUT = list()
tcga_neg_NDUT = list()
tcga_nor_NDUT = list()

p_max = [0, 0, 0, 0, 0, 0] # max for all recordings (curtis, vande, gluck, chin, tcga)
p_min = [0, 0, 0, 0, 0, 0] # min for all recordings
p_med = [0, 0, 0, 0, 0, 0] # overall median
p_q1 = [0, 0, 0, 0, 0, 0] # lower quartile
p_q3 = [0, 0, 0, 0, 0, 0] # upper quartile
# -----------
# Negative Grouping
n_max = [0, 0, 0, 0, 0, 0]
n_min = [0, 0, 0, 0, 0, 0]
n_med = [0, 0, 0, 0, 0, 0]
n_q1 = [0, 0, 0, 0, 0, 0]
n_q3 = [0, 0, 0, 0, 0, 0]
# -----------
# Normal Grouping
nor_max = [0, 0, 0, 0, 0, 0]
nor_min = [0, 0, 0, 0, 0, 0]
nor_med = [0, 0, 0, 0, 0, 0]
nor_q1 = [0, 0, 0, 0, 0, 0]
nor_q3 = [0, 0, 0, 0, 0, 0]


# CURTIS
print "--------------------\n\n\nCURTIS BREAST DETAIL\n"

#def read_csv(): # read in data from the csv file	
with open("Curtis_Breast_Detail_1.csv") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")
    offset = 0
    for row in csvReader:
        if offset > 1:
            if row[5] == "Breast" and row[5] != "Breast Carcinoma" and row[5] != "Invasive Breast Carcinoma":
                curtis_nor_NDUT.append(float(row[103]))
            if row[22] == "Estrogen Receptor Positive":
                curtis_pos_NDUT.append(float(row[103]))
            if row[22] == "Estrogen Receptor Negative":
                curtis_neg_NDUT.append(float(row[103]))    
                    # curtis_r_pn.append(0) # append zeros to the ratio list for modification later
        elif offset == 1:
            print row[22], "\t", row[103], "\n"
        offset += 1


# vandeVijver
print "--------------------\n\n\nVANDEVIJVER BREAST DETAIL\n"

#def read_csv(): # read in data from the csv file	
with open("vandeVijver_Breast_Detail.csv") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")
    offset = 0
    for row in csvReader:
        if offset > 1:
            if row[4] == "Estrogen Receptor Positive":
                vande_pos_NDUT.append(float(row[32]))
            if row[4] == "Estrogen Receptor Negative":
                vande_neg_NDUT.append(float(row[32]))    
                    # curtis_r_pn.append(0) # append zeros to the ratio list for modification later
        elif offset == 1:
            print row[4], "\t", row[32], "\n"
        offset += 1


# gluck
print "--------------------\n\n\nGLUCK BREAST DETAIL\n"

#def read_csv(): # read in data from the csv file	
with open("Gluck_Breast_Detail.csv") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")
    offset = 0
    for row in csvReader:
        if offset > 1:
            if row[2] == "Breast" and row[2] != "Breast Carcinoma" and row[2] != "Invasive Breast Carcinoma":
                gluck_nor_NDUT.append(float(row[28]))
            if row[7] == "Estrogen Receptor Positive":
                gluck_pos_NDUT.append(float(row[28]))
            if row[7] == "Estrogen Receptor Negative":
                gluck_neg_NDUT.append(float(row[28]))    
                    # curtis_r_pn.append(0) # append zeros to the ratio list for modification later
        elif offset == 1:
            print row[7], "\t", row[28], "\n"
        offset += 1


# Chin
print "--------------------\n\n\nCHIN BREAST DETAIL\n"

#def read_csv(): # read in data from the csv file	
with open("Chin_Breast_2_Detail.csv") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")
    offset = 0
    for row in csvReader:
        if offset > 1:
            if row[9] == "Estrogen Receptor Positive":
                chin_pos_NDUT.append(float(row[47]))
            if row[9] == "Estrogen Receptor Negative":
                chin_neg_NDUT.append(float(row[47]))    
                    # curtis_r_pn.append(0) # append zeros to the ratio list for modification later
        elif offset == 1:
            print row[9], "\t", row[47], "\n"
        offset += 1
        
# TCGA        
print "--------------------\n\n\nTCGA BREAST DETAIL\n"

#def read_csv(): # read in data from the csv file	
with open("tcga.csv") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")
    offset = 0
    for row in csvReader:
        if offset > 1:
            if row[12] == "Breast" and (row[12] != "Breast Carcinoma" and row[12] != "Invasive Breast Carcinoma") or row[12] == "":
                tcga_nor_NDUT.append(float(row[69]))
            if row[23] == "Estrogen Receptor Positive":
                tcga_pos_NDUT.append(float(row[69]))
            if row[23] == "Estrogen Receptor Negative":
                tcga_neg_NDUT.append(float(row[69]))    
                    # curtis_r_pn.append(0) # append zeros to the ratio list for modification later
        elif offset == 1:
            print row[23], "\t", row[69], "\n"
        offset += 1

print "--------------------\n\tProcessing\n--------------------\n\tData\n--------------------\n"        
# Properly reading in data now
# ---------------------------
curtis_pos_NDUT.sort()
curtis_neg_NDUT.sort()
curtis_nor_NDUT.sort()
vande_pos_NDUT.sort()
vande_neg_NDUT.sort()
vande_nor_NDUT.sort()
gluck_pos_NDUT.sort()
gluck_neg_NDUT.sort()
gluck_nor_NDUT.sort()
chin_pos_NDUT.sort()
chin_neg_NDUT.sort()
chin_nor_NDUT.sort()
tcga_nor_NDUT.sort()
tcga_pos_NDUT.sort()

# ------------------
curtis_i_p = ca.median_set(curtis_pos_NDUT) # find the median index of the set
curtis_i_n = ca.median_set(curtis_neg_NDUT)
curtis_i_nor = ca.median_set(curtis_nor_NDUT)
# -----------
vande_i_p = ca.median_set(vande_pos_NDUT)
vande_i_n = ca.median_set(vande_neg_NDUT)
# -----------
gluck_i_p = ca.median_set(gluck_pos_NDUT)
gluck_i_n = ca.median_set(gluck_neg_NDUT)
gluck_i_nor = ca.median_set(gluck_nor_NDUT)
# -----------
chin_i_p = ca.median_set(chin_pos_NDUT)
chin_i_n = ca.median_set(chin_neg_NDUT)
# -----------
tcga_i_p = ca.median_set(tcga_pos_NDUT)
tcga_i_n = ca.median_set(tcga_neg_NDUT)
tcga_i_nor = ca.median_set(tcga_nor_NDUT)
# -----------------------------------------
# CURTIS
# -----------------------------------------
p_med[0] = ca.median_value(curtis_i_p, curtis_pos_NDUT)
n_med[0] = ca.median_value(curtis_i_n, curtis_neg_NDUT)
nor_med[0] = ca.median_value(curtis_i_nor, curtis_nor_NDUT)
# -----------------------------------------
# VANDE
# -----------------------------------------
p_med[1] = ca.median_value(vande_i_p, vande_pos_NDUT)
n_med[1] = ca.median_value(vande_i_n, vande_neg_NDUT)
# -----------------------------------------
# GLUCK
# -----------------------------------------
p_med[2] = ca.median_value(gluck_i_p, gluck_pos_NDUT)
n_med[2] = ca.median_value(gluck_i_n, gluck_neg_NDUT)
nor_med[2] = ca.median_value(gluck_i_nor, gluck_pos_NDUT)
# -----------------------------------------
# CHIN
# -----------------------------------------
p_med[3] = ca.median_value(chin_i_p, chin_pos_NDUT)
n_med[3] = ca.median_value(chin_i_n, chin_neg_NDUT)
# -----------------------------------------
# TCGA
# -----------------------------------------
p_med[4] = ca.median_value(tcga_i_p, tcga_pos_NDUT)
n_med[4] = ca.median_value(tcga_i_n, tcga_neg_NDUT)
nor_med[4] = ca.median_value(tcga_i_nor, tcga_nor_NDUT)
print "RESLUTS:\n---------------------\nFirst Median:\n", "curtis_p_med[0]: ", p_med[0], "\tcurtis_n_med[0]: ", n_med[0], "\ncurtis_nor_med[0]: ", nor_med[0], "\nvande_p_med[0]: ", p_med[1], "\tvande_n_med[0]: ", n_med[1], "\ngluck_p_med[0]: ", p_med[2], "\tgluck_n_med[0]: ", n_med[2], "\ngluck_nor_med[0]: ", nor_med[2], "\nchin_p_med[0]: ", p_med[3], "\tchin_n_med[0]: ", n_med[3], "\ntcga_p_med[0]: ", p_med[4], "\ttcga_n_med[0]: ", n_med[4], "\ntcga_nor_med[0]: ", nor_med[4]  
# -----------
# Finding the lower quartile
# -----------
# -----------------------------------------
# CURTIS
# -----------------------------------------
p_q1[0] = ca.lower_quartile_find(curtis_i_p, curtis_pos_NDUT)
n_q1[0] = ca.lower_quartile_find(curtis_i_n, curtis_neg_NDUT)
nor_q1[0] = ca.lower_quartile_find(curtis_i_nor, curtis_nor_NDUT)
# -----------------------------------------
# VANDE
# -----------------------------------------
p_q1[1] = ca.lower_quartile_find(vande_i_p, vande_pos_NDUT)
n_q1[1] = ca.lower_quartile_find(vande_i_n, vande_neg_NDUT)
# -----------------------------------------
# GLUCK
# -----------------------------------------
p_q1[2] = ca.lower_quartile_find(gluck_i_p, gluck_pos_NDUT)
n_q1[2] = ca.lower_quartile_find(gluck_i_n, gluck_neg_NDUT)
nor_q1[2] = ca.lower_quartile_find(gluck_i_nor, gluck_nor_NDUT)
# -----------------------------------------
# CHIN
# -----------------------------------------
p_q1[3] = ca.lower_quartile_find(chin_i_p, chin_pos_NDUT)
n_q1[3] = ca.lower_quartile_find(chin_i_n, chin_neg_NDUT)
# -----------------------------------------
# TCGA
# -----------------------------------------
p_q1[4] = ca.lower_quartile_find(tcga_i_p, tcga_pos_NDUT)
n_q1[4] = ca.lower_quartile_find(tcga_i_n, tcga_neg_NDUT)
nor_q1[4] = ca.lower_quartile_find(tcga_i_nor, tcga_nor_NDUT)
# -----------------------------------------
print "---------------------\nLower Quartile:\n", "curtis_pq_1: ", p_q1[0], "\t", "curtis_nq_1: ", n_q1[0], "\ncurtis_nor_q1: ", nor_q1[0], "\nvande_p_q1: ", p_q1[1], "\tvande_nq_1: ", n_q1[1], '\ngluck_p_q1: ', p_q1[2], "\tgluck_n_q1[0]: ", n_q1[2], "\ngluck_nor_q1[0]: ", nor_q1[2], "\nchin_p_q1: ", p_q1[3], "\tchin_n_q1: ", n_q1[3], "\ntcga_p_q1[0]: ", p_q1[4], "\ttcga_n_q1[0]: ", n_q1[4], "\ntcga_nor_q1[0]: ", nor_med[4]
# -----------
# Finding the upper quartile
# -----------
# -----------------------------------------
# CURTIS
# -----------------------------------------
p_q3[0] = ca.upper_quartile_find(curtis_i_p, curtis_pos_NDUT)
n_q3[0] = ca.upper_quartile_find(curtis_i_n, curtis_neg_NDUT)
nor_q3[0] = ca.upper_quartile_find(curtis_i_nor, curtis_nor_NDUT)
# -----------------------------------------
# VANDE
# -----------------------------------------
p_q3[1] = ca.upper_quartile_find(vande_i_p, vande_pos_NDUT)
n_q3[1] = ca.upper_quartile_find(vande_i_n, vande_neg_NDUT)
# -----------------------------------------
# GLUCK
# -----------------------------------------
p_q3[2] = ca.upper_quartile_find(gluck_i_p, gluck_pos_NDUT)
n_q3[2] = ca.upper_quartile_find(gluck_i_n, gluck_neg_NDUT)
nor_q3[2] = ca.upper_quartile_find(gluck_i_nor, gluck_nor_NDUT)
# -----------------------------------------
# CHIN
# -----------------------------------------
p_q3[3] = ca.upper_quartile_find(chin_i_p, chin_pos_NDUT)
n_q3[3] = ca.upper_quartile_find(chin_i_n, chin_neg_NDUT)
# -----------------------------------------
# TCGA
# -----------------------------------------
p_q3[4] = ca.upper_quartile_find(tcga_i_p, tcga_pos_NDUT)
n_q3[4] = ca.upper_quartile_find(tcga_i_n, tcga_neg_NDUT)
nor_q3[4] = ca.upper_quartile_find(tcga_i_nor, tcga_nor_NDUT)       
print "---------------------\nUpper Quartile:\n", "curtis_pq_3: ", p_q3[0], "\t", "curtis_nq_3: ", n_q3[0] , "\nnorq_3: ", nor_q3[0], "\nvande_p_q3: ", p_q3[1], "\tvande_n_q3: ", n_q3[1], "\ngluck_p_q3: ", p_q3[2], "\tgluck_n_q3: ", n_q3[2], "\ngluck_nor_q3: ", nor_q3[2], "\nchin_p_q3: ", p_q3[3], "\tchin_n_q3: ", n_q3[3], "\ntcga_p_q3: ", p_q3[4], "\ttcga_n_q3: ", n_q3[4], "\ntcga_nor_q3: ", nor_q3[4]       
# -----------------------------------------
# RECORDING MAX AND MIN VALUES
# -----------------------------------------
p_max[0] = max(curtis_pos_NDUT)
p_min[0] = min(curtis_pos_NDUT)
n_max[0] = max(curtis_neg_NDUT)
n_min[0] = min(curtis_neg_NDUT)
nor_max[0] = max(curtis_nor_NDUT)
nor_min[0] = min(curtis_nor_NDUT)
p_max[1] = max(vande_pos_NDUT)
p_min[1] = min(vande_pos_NDUT)
n_max[1] = max(vande_neg_NDUT)
n_min[1] = min(vande_neg_NDUT)
p_max[2] = max(gluck_pos_NDUT)
p_min[2] = min(gluck_pos_NDUT)
n_max[2] = max(gluck_neg_NDUT)
n_min[2] = min(gluck_neg_NDUT)
nor_max[2] = max(gluck_nor_NDUT)
nor_min[2] = min(gluck_nor_NDUT)
p_max[3] = max(chin_pos_NDUT)
p_min[3] = min(chin_pos_NDUT)
n_max[3] = max(chin_neg_NDUT)
n_min[3] = min(chin_neg_NDUT)
p_max[4] = max(tcga_pos_NDUT)
p_min[4] = min(tcga_pos_NDUT)
n_max[4] = max(tcga_neg_NDUT)
n_min[4] = min(tcga_neg_NDUT)
nor_max[4] = max(tcga_nor_NDUT)
nor_min[4] = min(tcga_nor_NDUT)

r = open("outfile.txt", "w")
mod = str(p_max[0])  + "\t" +  str(p_max[1]) + "\t" + str(p_max[2]) + "\t" +  str(p_max[3])+ "\t" + str(p_max[4])   + "\t" + str(n_max[0])  + "\t" + str(n_max[1])   + "\t" + str(n_max[2])   + "\t" + str(n_max[3])   + "\t" + str(n_max[4])   + "\t" + str(nor_max[0])   + "\t" + str(nor_max[2])   + "\t" + str(nor_max[4])   + "\n" + str(p_q1[0])  + "\t" + str(p_q1[1]) + "\t" + str(p_q1[2])  + "\t" + str(p_q1[3])   + "\t" + str(p_q1[4])  + "\t" + str(n_q1[0])  + "\t" + str(n_q1[1]) + "\t" + str(n_q1[2])  + "\t" + str(n_q1[3])  + "\t" + str(n_q1[4])   + "\t" + str(nor_q1[0])  + "\t" + str(nor_q1[2])  + "\t" + str(nor_q1[4]) + "\n" +  str(p_q3[0])  + "\t" + str(p_q3[1])  + "\t" + str(p_q3[2])  + "\t" + str(p_q3[3])  + "\t" + str(p_q3[4])  + "\t" + str(n_q3[0])  + "\t" + str(n_q3[1])   + "\t" + str(n_q3[2])  + "\t" + str(n_q3[3])  + "\t" + str(n_q3[4])   + "\t" + str(nor_q3[0])   + "\t" + str(nor_q3[2])   + "\t" + str(nor_q3[4]) + "\n" +  str(p_med[0])   + "\t" + str(p_med[1])  + "\t" + str(p_med[2])  + "\t" + str(p_med[3])  + "\t" + str(p_med[4])  + "\t" + str(n_med[0])  + "\t" + str(n_med[1])  + "\t" + str(n_med[2])  + "\t" + str(n_med[3]) + "\t" + str(n_med[4])  + "\t" + str(nor_med[0])   + "\t" + str(nor_med[2])  + "\t" + str(nor_med[4]) + "\n" +  str(p_min[0])  + "\t" + str(p_min[1])  + "\t" + str(p_min[2])  + "\t" + str(p_min[3])   + "\t" + str(p_min[4])  + "\t" + str(n_min[0])  + "\t" + str(n_min[1])  + "\t" + str(n_min[2])  + "\t" + str(n_min[3]) + "\t" + str(n_min[4])  + "\t" + str(nor_min[0])  + "\t" + str(n_min[2])  + "\t" + str(nor_min[4]) 
r.write(mod)
r.close()

#print "len(curtis_nor_NDUT): ", len(curtis_nor_NDUT)

for i in range(1364):
    curtis_nor_NDUT.append(50)

#print "len(curtis_pos_NDUT): ", len(curtis_pos_NDUT), "\tlen(curtis_neg_NDUT): ", len(curtis_neg_NDUT), "\nlen(curtis_nor_NDUT) :"

f = open("new_data.txt", 'w')

for i in range(len(curtis_pos_NDUT)):
    
    if i >= len(curtis_neg_NDUT):
        curtis_neg_NDUT.append(50)
        #print "appending\n"
        
    if i >= len(curtis_nor_NDUT):
        curtis_neg_NDUT.append(50)
        # print "appending\n"
        
    if i >= len(vande_pos_NDUT):
        vande_pos_NDUT.append(50)
        
    if i >= len(vande_neg_NDUT):
        vande_neg_NDUT.append(50)
        
    if i >= len(gluck_pos_NDUT):
        gluck_pos_NDUT.append(50)
        
    if i >= len(gluck_neg_NDUT):
        gluck_neg_NDUT.append(50)
        
    if i >= len(gluck_nor_NDUT):
        gluck_nor_NDUT.append(50)
        
    if i >= len(chin_pos_NDUT):
        chin_pos_NDUT.append(50)
        
    if i >= len(chin_neg_NDUT):
        chin_neg_NDUT.append(50)
        
    if i >= len(tcga_pos_NDUT):
        tcga_pos_NDUT.append(50)
        
    if i >= len(tcga_neg_NDUT):
        tcga_neg_NDUT.append(50)
        
    if i >= len(tcga_nor_NDUT):
        tcga_nor_NDUT.append(50)
        


word = str(curtis_pos_NDUT[1]) + "\t" + str(curtis_neg_NDUT[1]) + "\t" + str(curtis_nor_NDUT[1])
#print word

#print len(curtis_pos_NDUT), "\t", len(curtis_nor_NDUT), "\t", len(vande_pos_NDUT), "\n", len(vande_neg_NDUT), "\t", len(gluck_pos_NDUT), "\t", len(gluck_neg_NDUT), "\n", len(gluck_nor_NDUT), "\t", len(chin_pos_NDUT), "\t", len(chin_neg_NDUT), "\n", len(tcga_pos_NDUT), "\t", len(tcga_neg_NDUT), "\t", len(tcga_nor_NDUT), "\n"

for i in range(len(curtis_pos_NDUT)):
    mod = str(curtis_pos_NDUT[i]) + "\t" + str(curtis_neg_NDUT[i]) + "\t" + str(curtis_nor_NDUT[i]) + "\t" + str(vande_pos_NDUT[i]) + "\t" + str(vande_neg_NDUT[i]) + "\t" + str(gluck_pos_NDUT[i]) + "\t" + str(gluck_neg_NDUT[i]) + "\t" + str(gluck_nor_NDUT[i]) + "\t" + str(chin_pos_NDUT[i]) + "\t" + str(chin_neg_NDUT[i]) + "\t" + str(tcga_pos_NDUT[i]) + "\t" + str(tcga_neg_NDUT[i]) + "\t" + str(tcga_nor_NDUT[i])+ "\n"
    f.write(mod)
