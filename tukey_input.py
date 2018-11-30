# Code to generate input data for Tukyey's HSD analysis and plots with TukHSD package in R, using FFC output files. 
# Written by Noelle Patterson, UC Davis Water Management Lab, fall 2018

import glob
import numpy as np
import csv
import math
import pandas as pd
from Utils.sortGages import sortGages
from Utils.convertDateType import convertJulianToOffset

files = glob.glob("All-Results/*_annual_result_matrix.csv")
classes = sortGages(files)
class_label = []
all_metrics = {}
Avg = []
CV = []
SP_Tim = []
DS_Tim = []
DS_Mag_10 = []
DS_Dur_WSI = []
Wet_Tim = []
Wet_BFL_Mag = []
Peak_Fre_10 = []
Peak_Fre_20 = []
WSI_Mag = []
WSI_Tim = []

for currentClass, value in classes.items():
    for i, annual in enumerate (value):
        for index, subyear in enumerate(annual):
            Avg.append(annual.loc['Avg'][index])
            CV.append(annual.loc['CV'][index])
            SP_Tim.append(annual.loc['SP_Tim'][index])
            DS_Tim.append(annual.loc['DS_Tim'][index])
            DS_Mag_10.append(annual.loc['DS_Mag_10'][index])
            DS_Dur_WSI.append(annual.loc['DS_Dur_WSI'][index])
            Wet_Tim.append(annual.loc['Wet_Tim'][index])
            Wet_BFL_Mag.append(annual.loc['Wet_BFL_Mag'][index])
            Peak_Fre_10.append(annual.loc['Peak_Fre_10'][index])
            Peak_Fre_20.append(annual.loc['Peak_Fre_20'][index])
            WSI_Mag.append(annual.loc['WSI_Mag'][index])
            WSI_Tim.append(annual.loc['WSI_Tim'][index])
            class_label.append(int(currentClass[-1])) # create list with class label to keep track of each row's class

for i in range(len(Wet_Tim)):
    Wet_Tim[i] = convertJulianToOffset(Wet_Tim[i], 1995)
    SP_Tim[i] = convertJulianToOffset(SP_Tim[i], 1995)
    DS_Tim[i] = convertJulianToOffset(DS_Tim[i], 1995)
    WSI_Tim[i] = convertJulianToOffset(WSI_Tim[i], 1995)
    # Peak_Tim_2[i] = convertJulianToOffset(Peak_Tim_2[i], 1995)

 """To plot only the 10th to 90th percentile results uncomment block below"""
    # low = 10
    # high = 90
    # for currentClass in classes: 
    #     Avg = [np.nan if ele < np.nanpercentile(Avg, low) or ele > np.nanpercentile(Avg, high) else ele for index, ele in enumerate(Avg)]

class_names = ["1-SM", "2-HSR", "3-LSR", "4-WS", "5-GW", "6-PGR", "7-FER", "8-RGW", "9-HLP"]
newArray = [class_names[item - 1] for item in class_label]   

csv_outputs = [newArray, Avg, CV, SP_Tim, DS_Tim, DS_Mag_10, DS_Dur_WSI, Wet_Tim, Wet_BFL_Mag, Peak_Fre_10, Peak_Fre_20, WSI_Mag, WSI_Tim]
csv_outputs_transpose = list(map(list, zip(*csv_outputs)))
header = ['groups', 'Avg', 'CV', 'SP_Tim', 'DS_Tim', 'DS_Mag_10', 'DS_Dur_WSI', 'Wet_Tim', 'Wet_BFL_Mag', 'Peak_Fre_10', 'Peak_Fre_20', 'WSI_Mag', 'WSI_Tim']

with open('tukey_input.csv', 'w') as csvfile:
    resultsWriter = csv.writer(csvfile, dialect='excel')
    resultsWriter.writerows(csv_outputs_transpose)

from pandas import read_csv
df = read_csv('tukey_input.csv')
df.columns = header
df.to_csv('tukey_input.csv', index=False)