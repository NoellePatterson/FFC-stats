import numpy as np
from Utils.convertDateType import convertJulianToOffset, convertOffsetToJulianSingle

def calcSpreadMetrics(classes, resultsName):
    timingSD = {}
    timing10 = {}
    timing90 = {}
    for currentClass, value in classes.items(): # loop through all nine classes
        SDlist = []
        for i, results in enumerate(value):
            SDlist.append(value[i].loc[resultsName])

        flatSDlist = []
        for sublist in SDlist:
            for index, item in enumerate(sublist):
                if np.isnan(item) == False:
                    year = int(sublist.index[index])
                    offsetTim = convertJulianToOffset(item, year)
                    flatSDlist.append(offsetTim)
        if currentClass in timingSD:
            timingSD[currentClass].append(flatSDlist)
        else:
            timingSD[currentClass] = flatSDlist
            timing10[currentClass] = convertOffsetToJulianSingle(np.nanpercentile(flatSDlist, 10),1995)
            timing90[currentClass] = convertOffsetToJulianSingle(np.nanpercentile(flatSDlist, 90),1995) 

    for currentClass in timingSD:
        timingSD[currentClass] = np.nanstd(timingSD[currentClass])

    return timingSD, timing10, timing90
