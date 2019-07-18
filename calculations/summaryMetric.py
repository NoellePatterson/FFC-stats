import numpy as np
from Utils.convertDateType import convertJulianToOffsetSingle, convertOffsetToJulianSingle

def summaryMetric(classes):
    summaryMetric = {} 
    all_vals = [] # Need to compile all results from relevant classes, and then take average. 
    for currentClass, value in classes.items(): # loop through all nine classes
        # all_vals = []
        # snowmelt
        # if currentClass == 'class2' or currentClass == 'class3' or currentClass == 'class5' or currentClass == 'class4' or currentClass == 'class6' or currentClass == 'class7' or currentClass == 'class8':
        # mixed
        # if currentClass == 'class1' or currentClass == 'class4' or currentClass == 'class6' or currentClass == 'class7' or currentClass == 'class8' or currentClass == 'class9':
        # rain
        if currentClass == 'class1' or currentClass == 'class9' or currentClass == 'class2' or currentClass == 'class3' or currentClass == 'class9':
            continue
        Avg = [] # Compile results for each class, first
        for i, results in enumerate (value):
            Avg.append(value[i].loc['Wet_Tim']) # insert whatever misc. metric needs to be summarized here 
 
    #     """Use this block if date converting is not needed"""
    #     for index, gage in enumerate(Avg): # loop through each gage (223)
    #         Avgsummary = np.nanmean(gage)               
    #         if currentClass in summaryMetric:
    #             summaryMetric[currentClass].append(Avgsummary)    
    #         else:
    #             summaryMetric[currentClass] = [Avgsummary] 
    # for currentClass in summaryMetric: 
    #     summaryMetric[currentClass] = np.nanmean(summaryMetric[currentClass])

        """Use this block for date converting"""
        for sublist in Avg:
            for index, item in enumerate(sublist):
                if np.isnan(item) == False:
                    year = 1995
                    offsetTim = convertJulianToOffsetSingle(item, year)
                    all_vals.append(offsetTim)
    #                 """For class averages"""
    #                 if currentClass in summaryMetric:
    #                     summaryMetric[currentClass].append(offsetTim)    
    #                 else:
    #                     summaryMetric[currentClass] = [offsetTim]
    # for currentClass in summaryMetric: 
    #     summaryMetric[currentClass] = np.nanmean(summaryMetric[currentClass])    
    offset_mean = np.nanmean(all_vals)
    summaryMetric[currentClass] = convertOffsetToJulianSingle(offset_mean, 1995)
        
    return summaryMetric
