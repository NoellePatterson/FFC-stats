import numpy as np
from Utils.convertDateType import convertOffsetToJulian

def rainLateBfl(classes):
    rainLateBfl = {}
    for currentClass, value in classes.items():
        sumTim = []

        for i, results in enumerate(value): # loop through each gage
            sumTim.append(value[i].loc['DS_Tim'])

        for index, gage in enumerate(sumTim): # loop through sum val's for each gage (223)
            counter = 0
            allWaterYears = 0
            year = int(gage.index[0])
            for i, flow in enumerate(gage): # go through each year in the gage
                if np.isnan(sumTim[index][i]) == False:
                    allWaterYears = allWaterYears + 1

                    offsetSumTim = [int(sumTim[index][i])]
                    offsetSumTim = convertOffsetToJulian(offsetSumTim, year)
                    if offsetSumTim[0] > 305: # check if summer date is later than August 1st
                        counter = counter + 1

            if currentClass in rainLateBfl:
                rainLateBfl[currentClass].append(counter/allWaterYears)
            else:
                rainLateBfl[currentClass] = [counter/allWaterYears]

    for currentClass in rainLateBfl:
        rainLateBfl[currentClass] = np.nanmean(rainLateBfl[currentClass])
    rainLateBfl['class1'] = None
    rainLateBfl['class2'] = None
    rainLateBfl['class3'] = None
    rainLateBfl['class5'] = None
    rainLateBfl['class9'] = None
    return rainLateBfl
