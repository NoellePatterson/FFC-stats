import numpy as np
from Utils.convertDateType import convertJulianToOffsetSingle, convertOffsetToJulianSingle

def calcSpreadMetrics(classes, resultsName):
    timingSD = {}
    timing10 = {}
    timing90 = {}
    roc10 = {}
    roc90 = {}
    for currentClass, value in classes.items(): # loop through all nine classes
        SDlist = []
        roclist = []
        for i, results in enumerate(value):
            SDlist.append(value[i].loc[resultsName])
            roclist.append(value[i].loc['SP_ROC'])

        flatSDlist = []
        flatROClist = []
        for sublist in SDlist:
            for index, item in enumerate(sublist):
                if np.isnan(item) == False:
                    year = int(sublist.index[index])
                    offsetTim = convertJulianToOffsetSingle(item, year)
                    flatSDlist.append(offsetTim)
        for sublist in roclist:
            for index, item in enumerate(sublist):
                if np.isnan(item) == False:
                    flatROClist.append(item)
        if currentClass in timingSD:
            timingSD[currentClass].append(flatSDlist)
        else:
            timingSD[currentClass] = flatSDlist
            timing10[currentClass] = convertOffsetToJulianSingle(np.nanpercentile(flatSDlist, 10),1995)
            timing90[currentClass] = convertOffsetToJulianSingle(np.nanpercentile(flatSDlist, 90),1995) 
            roc10[currentClass] = np.nanpercentile(flatROClist, 10)
            roc90[currentClass] = np.nanpercentile(flatROClist, 90)
    for currentClass in timingSD:
        timingSD[currentClass] = np.nanstd(timingSD[currentClass])

    return timingSD, timing10, timing90, roc10, roc90
