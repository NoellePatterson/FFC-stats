import numpy as np

def LSRstandardDev(LSRresults):
    standardDev = []
    for i, results in enumerate(LSRresults):
        standardDev.append(LSRresults[i].loc['Std'])
    
    finalSDarray = []    
    for index, gage in enumerate(standardDev): # loop through each gage
        sdBelowOne = 0
        totalYears = len(standardDev[index])
        for i, year in enumerate(gage): # go through each year in the gage
            if standardDev[index][i] < 1:
                sdBelowOne = sdBelowOne + 1
        finalSDarray.append(sdBelowOne/totalYears)  
    
    LSRstandardDev = {}
    LSRstandardDev['class3'] = np.nanmean(finalSDarray)
    LSRstandardDev['class1'] = None
    LSRstandardDev['class2'] = None
    LSRstandardDev['class4'] = None
    LSRstandardDev['class5'] = None
    LSRstandardDev['class6'] = None
    LSRstandardDev['class7'] = None
    LSRstandardDev['class8'] = None
    LSRstandardDev['class9'] = None
    
    return LSRstandardDev

