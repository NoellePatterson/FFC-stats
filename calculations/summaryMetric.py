import numpy as np
from Utils.convertDateType import convertJulianToOffset, convertOffsetToJulianSingle

def summaryMetric(classes):
    summaryMetric = {} 
    for currentClass, value in classes.items(): # loop through all nine classes
        Avg = [] 
        for i, results in enumerate (value):
            Avg.append(value[i].loc['DS_Tim']) # insert whatever misc. metric needs to be summarized here 
 
    #     """Use this block is date converting is not needed"""
    #     for index, gage in enumerate(Avg): # loop through each gage (223)
    #         Avgsummary = np.nanmean(gage)               
    #         if currentClass in summaryMetric:
    #             summaryMetric[currentClass].append(Avgsummary)    
    #         else:
    #             summaryMetric[currentClass] = [Avgsummary] 
    # for currentClass in summaryMetric: 
    #     summaryMetric[currentClass] = np.nanpercentile(summaryMetric[currentClass], 50)

        """Use this block is date converting is needed"""
        convertList = []
        for sublist in Avg:
            for index, item in enumerate(sublist):
                if np.isnan(item) == False:
                    year = 1995
                    offsetTim = convertJulianToOffset(item, year)
                    convertList.append(offsetTim)
        avg_julian = convertOffsetToJulianSingle(np.nanmean(convertList), year)
        summaryMetric[currentClass] = avg_julian
        
    return summaryMetric
