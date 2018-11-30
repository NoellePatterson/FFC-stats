import numpy as np

def summaryMetric(classes):
    summaryMetric = {} 
    for currentClass, value in classes.items(): # loop through all nine classes
        Avg = [] # insert whatever misc. metric needs to be summarized here
        for i, results in enumerate (value):
            Avg.append(value[i].loc['DS_Tim']) # insert whatever misc. metric needs to be summarized here 

        for index, gage in enumerate(Avg): # loop through each gage (223)
            Avgsummary = np.nanmean(gage)            
            
            if currentClass in summaryMetric:
                summaryMetric[currentClass].append(Avgsummary)    
            else:
                summaryMetric[currentClass] = [Avgsummary] 
    
    for currentClass in summaryMetric: 
        # summaryMetric[currentClass] = np.nanpercentile(summaryMetric[currentClass], 50)
        summaryMetric[currentClass] = np.nanmean(summaryMetric[currentClass])
        
    return summaryMetric
