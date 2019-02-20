# Code to generate input data for Tukyey's HSD analysis and plots with TukHSD package in R, using FFC output files. 
# Written by Noelle Patterson, UC Davis Water Management Lab, fall 2018
# Dictionary structure: input data is classes dict containing class keys with all results info.
# Output data is classes_results dict with class keys pointing to class dictionaries
# Individual class dictionaries have keys for each metric and values with all vals. 

import glob
import numpy as np
import csv
import math
import pandas as pd
import itertools
from Utils.sortGages import sortGages
from Utils.convertDateType import convertJulianToOffset

files = glob.glob("All-Results/*_annual_result_matrix.csv")
classes = sortGages(files)
class_label = []
class_results = {}

for currentClass, value in classes.items():
    class_results[currentClass] = {'Avg': [], 'CV':[], 'SP_Tim':[], 'DS_Tim':[], 'DS_Mag_10':[], 'DS_Dur_WSI':[],'DS_Dur_WS':[], 'Wet_Tim':[],\
    'Wet_BFL_Mag':[], 'Peak_Fre_10':[], 'Peak_Fre_20':[], 'WSI_Mag':[], 'WSI_Tim':[], 'WSI_Dur':[]}
    for i, annual in enumerate (value):
        for index, subyear in enumerate(annual):
            # import pdb; pdb.set_trace()
            class_results[currentClass]['Avg'].append(annual.loc['Avg'][index])
            class_results[currentClass]['CV'].append(annual.loc['CV'][index])
            class_results[currentClass]['SP_Tim'].append(annual.loc['SP_Tim'][index])
            class_results[currentClass]['DS_Tim'].append(annual.loc['DS_Tim'][index])
            class_results[currentClass]['DS_Mag_10'].append(annual.loc['DS_Mag_10'][index])
            class_results[currentClass]['DS_Dur_WSI'].append(annual.loc['DS_Dur_WSI'][index])
            class_results[currentClass]['DS_Dur_WS'].append(annual.loc['DS_Dur_WS'][index])
            class_results[currentClass]['Wet_Tim'].append(annual.loc['Wet_Tim'][index])
            class_results[currentClass]['Wet_BFL_Mag'].append(annual.loc['Wet_BFL_Mag'][index])
            class_results[currentClass]['Peak_Fre_10'].append(annual.loc['Peak_Fre_10'][index])
            class_results[currentClass]['Peak_Fre_20'].append(annual.loc['Peak_Fre_20'][index])
            class_results[currentClass]['WSI_Mag'].append(annual.loc['WSI_Mag'][index])
            class_results[currentClass]['WSI_Tim'].append(annual.loc['WSI_Tim'][index])
            class_results[currentClass]['WSI_Dur'].append(annual.loc['WSI_Dur'][index])
 
            class_label.append(int(currentClass[-1])) # create list with class label to keep track of each row's class
    """Convert calendar date outputs to offset dates for correct analysis"""
    for i in range(len(class_results[currentClass]['SP_Tim'])):  
        class_results[currentClass]['SP_Tim'][i] = convertJulianToOffset(class_results[currentClass]['SP_Tim'][i], 1995)
        class_results[currentClass]['Wet_Tim'][i] = convertJulianToOffset(class_results[currentClass]['Wet_Tim'][i], 1995)
        class_results[currentClass]['DS_Tim'][i] = convertJulianToOffset(class_results[currentClass]['DS_Tim'][i], 1995)
        class_results[currentClass]['WSI_Tim'][i] = convertJulianToOffset(class_results[currentClass]['WSI_Tim'][i], 1995)

    """To plot only the 10th to 90th percentile results uncomment block below"""
    # low = 10
    # high = 90
    # class_results[currentClass]['Avg'] = [np.nan if ele < np.nanpercentile(class_results[currentClass]['Avg'], low) or ele > np.nanpercentile(class_results[currentClass]['Avg'], high) else ele for index, ele in enumerate(class_results[currentClass]['Avg'])]
    # class_results[currentClass]['CV'] = [np.nan if ele < np.nanpercentile(class_results[currentClass]['CV'], low) or ele > np.nanpercentile(class_results[currentClass]['CV'], high) else ele for index, ele in enumerate(class_results[currentClass]['CV'])]
    # class_results[currentClass]['SP_Tim'] = [np.nan if ele < np.nanpercentile(class_results[currentClass]['SP_Tim'], low) or ele > np.nanpercentile(class_results[currentClass]['SP_Tim'], high) else ele for index, ele in enumerate(class_results[currentClass]['SP_Tim'])]
    # class_results[currentClass]['DS_Tim'] = [np.nan if ele < np.nanpercentile(class_results[currentClass]['DS_Tim'], low) or ele > np.nanpercentile(class_results[currentClass]['DS_Tim'], high) else ele for index, ele in enumerate(class_results[currentClass]['DS_Tim'])]
    # class_results[currentClass]['DS_Mag_10'] = [np.nan if ele < np.nanpercentile(class_results[currentClass]['DS_Mag_10'], low) or ele > np.nanpercentile(class_results[currentClass]['DS_Mag_10'], high) else ele for index, ele in enumerate(class_results[currentClass]['DS_Mag_10'])]
    # class_results[currentClass]['DS_Dur_WSI'] = [np.nan if ele < np.nanpercentile(class_results[currentClass]['DS_Dur_WSI'], low) or ele > np.nanpercentile(class_results[currentClass]['DS_Dur_WSI'], high) else ele for index, ele in enumerate(class_results[currentClass]['DS_Dur_WSI'])]
    # class_results[currentClass]['Wet_Tim'] = [np.nan if ele < np.nanpercentile(class_results[currentClass]['Wet_Tim'], low) or ele > np.nanpercentile(class_results[currentClass]['Wet_Tim'], high) else ele for index, ele in enumerate(class_results[currentClass]['Wet_Tim'])]
    # class_results[currentClass]['Wet_BFL_Mag'] = [np.nan if ele < np.nanpercentile(class_results[currentClass]['Wet_BFL_Mag'], low) or ele > np.nanpercentile(class_results[currentClass]['Wet_BFL_Mag'], high) else ele for index, ele in enumerate(class_results[currentClass]['Wet_BFL_Mag'])]
    # class_results[currentClass]['Peak_Fre_10'] = [np.nan if ele < np.nanpercentile(class_results[currentClass]['Peak_Fre_10'], low) or ele > np.nanpercentile(class_results[currentClass]['Peak_Fre_10'], high) else ele for index, ele in enumerate(class_results[currentClass]['Peak_Fre_10'])]
    # class_results[currentClass]['Peak_Fre_20'] = [np.nan if ele < np.nanpercentile(class_results[currentClass]['Peak_Fre_20'], low) or ele > np.nanpercentile(class_results[currentClass]['Peak_Fre_20'], high) else ele for index, ele in enumerate(class_results[currentClass]['Peak_Fre_20'])]
    # class_results[currentClass]['WSI_Mag'] = [np.nan if ele < np.nanpercentile(class_results[currentClass]['WSI_Mag'], low) or ele > np.nanpercentile(class_results[currentClass]['WSI_Mag'], high) else ele for index, ele in enumerate(class_results[currentClass]['WSI_Mag'])]
    # class_results[currentClass]['WSI_Tim'] = [np.nan if ele < np.nanpercentile(class_results[currentClass]['WSI_Tim'], low) or ele > np.nanpercentile(class_results[currentClass]['WSI_Tim'], high) else ele for index, ele in enumerate(class_results[currentClass]['WSI_Tim'])]

"""Arrange class_results dictionary items into table format"""
for currentClass, value in class_results.items(): 
    if currentClass == 'class1' or currentClass == 'class9':
        label = [int(1)]*len(value['Avg'])
    if currentClass == 'class2' or currentClass == 'class3' or currentClass == 'class5':
        label = [int(2)]*len(value['Avg'])
    if currentClass == 'class4' or currentClass == 'class6' or currentClass == 'class7' or currentClass == 'class8':
        label = [int(3)]*len(value['Avg'])
    # label = [int(currentClass[-1])]*len(value['Avg'])
    Avg = value['Avg']
    CV = value['CV']
    SP_Tim = value['SP_Tim']
    DS_Tim = value['DS_Tim']
    DS_Mag_10 = value['DS_Mag_10']
    DS_Dur_WSI = value['DS_Dur_WSI']
    DS_Dur_WS = value['DS_Dur_WS']
    Wet_Tim = value['Wet_Tim']
    Wet_BFL_Mag = value['Wet_BFL_Mag']
    Peak_Fre_10 = value['Peak_Fre_10']
    Peak_Fre_20 = value['Peak_Fre_20']
    WSI_Mag = value['WSI_Mag']
    WSI_Tim = value['WSI_Tim']
    WSI_Dur = value['WSI_Dur']
    if currentClass == 'class1':
        class1_table = [label, Avg, CV, SP_Tim, DS_Tim, DS_Mag_10, DS_Dur_WSI, DS_Dur_WS, Wet_Tim, Wet_BFL_Mag, Peak_Fre_10, Peak_Fre_20, WSI_Mag, WSI_Tim, WSI_Dur]
    if currentClass == 'class2':
        class2_table = [label, Avg, CV, SP_Tim, DS_Tim, DS_Mag_10, DS_Dur_WSI, DS_Dur_WS, Wet_Tim, Wet_BFL_Mag, Peak_Fre_10, Peak_Fre_20, WSI_Mag, WSI_Tim, WSI_Dur]
    if currentClass == 'class3':
        class3_table = [label, Avg, CV, SP_Tim, DS_Tim, DS_Mag_10, DS_Dur_WSI, DS_Dur_WS, Wet_Tim, Wet_BFL_Mag, Peak_Fre_10, Peak_Fre_20, WSI_Mag, WSI_Tim, WSI_Dur]
    if currentClass == 'class4':
        class4_table = [label, Avg, CV, SP_Tim, DS_Tim, DS_Mag_10, DS_Dur_WSI, DS_Dur_WS, Wet_Tim, Wet_BFL_Mag, Peak_Fre_10, Peak_Fre_20, WSI_Mag, WSI_Tim, WSI_Dur]
    if currentClass == 'class5':
        class5_table = [label, Avg, CV, SP_Tim, DS_Tim, DS_Mag_10, DS_Dur_WSI, DS_Dur_WS, Wet_Tim, Wet_BFL_Mag, Peak_Fre_10, Peak_Fre_20, WSI_Mag, WSI_Tim, WSI_Dur]
    if currentClass == 'class6':
        class6_table = [label, Avg, CV, SP_Tim, DS_Tim, DS_Mag_10, DS_Dur_WSI, DS_Dur_WS, Wet_Tim, Wet_BFL_Mag, Peak_Fre_10, Peak_Fre_20, WSI_Mag, WSI_Tim, WSI_Dur]
    if currentClass == 'class7':
        class7_table = [label, Avg, CV, SP_Tim, DS_Tim, DS_Mag_10, DS_Dur_WSI, DS_Dur_WS, Wet_Tim, Wet_BFL_Mag, Peak_Fre_10, Peak_Fre_20, WSI_Mag, WSI_Tim, WSI_Dur]
    if currentClass == 'class8':
        class8_table = [label, Avg, CV, SP_Tim, DS_Tim, DS_Mag_10, DS_Dur_WSI, DS_Dur_WS, Wet_Tim, Wet_BFL_Mag, Peak_Fre_10, Peak_Fre_20, WSI_Mag, WSI_Tim, WSI_Dur]
    if currentClass == 'class9':
        class9_table = [label, Avg, CV, SP_Tim, DS_Tim, DS_Mag_10, DS_Dur_WSI, DS_Dur_WS, Wet_Tim, Wet_BFL_Mag, Peak_Fre_10, Peak_Fre_20, WSI_Mag, WSI_Tim, WSI_Dur]

total_table = zip(class1_table, class2_table, class3_table, class4_table, class5_table, class6_table, class7_table, class8_table, class9_table)  # stack results from each class so they all appear under one metric column
total_table = list(total_table) 
for index in range(len(total_table)): # condense each list of lists into one column per metric for output
    total_table[index] = list(itertools.chain(*total_table[index]))
# import pdb; pdb.set_trace()
class_names = ["1_Snowmelt", "2_Rain and Snowmelt", "3_Rain"]
total_table[0] = [class_names[item - 1] for item in total_table[0]]   
total_table_transpose = list(map(list, zip(*total_table)))

# total_sm = 0
# sm_wsi = 0
# total_rain = 0
# rain_wsi = 0
# total_mix = 0
# mix_wsi = 0
# for i, row in enumerate(total_table_transpose):
#     if row[0] == '1_Snowmelt':
#         total_sm+= 1 
#         if np.isnan(row[14]) == False:
#             sm_wsi += 1
#     if row[0] == '2_Rain and Snowmelt':
#         total_mix+= 1 
#         if np.isnan(row[14]) == False:
#             mix_wsi += 1
#     if row[0] == '3_Rain':
#         total_rain+= 1 
#         if np.isnan(row[14]) == False:
#             rain_wsi += 1

header = ['groups', 'Avg', 'CV', 'SP_Tim', 'DS_Tim', 'DS_Mag_10', 'DS_Dur_WSI', 'DS_Dur_WS', 'Wet_Tim', 'Wet_BFL_Mag', 'Peak_Fre_10', 'Peak_Fre_20', 'WSI_Mag', 'WSI_Tim', 'WSI_Dur']
import pdb; pdb.set_trace()
with open('tukey_input.csv', 'w') as csvfile:
    resultsWriter = csv.writer(csvfile, dialect='excel')
    resultsWriter.writerows(total_table_transpose)

from pandas import read_csv
df = read_csv('tukey_input.csv')
df.columns = header
df.to_csv('Outputs/tukey_input.csv', index=False)