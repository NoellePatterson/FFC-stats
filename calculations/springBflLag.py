import numpy as np
from Utils.convertDateType import convertJulianToOffset

def is_nan(x):
    return (x is np.nan or x != x)

def springBflLag(classes):
    springBflLag = {}
    for currentClass, value in classes.items(): # loop through all nine classes
        springTim = []
        sumTim = []

        for i, results in enumerate (value):
            springTim.append(value[i].loc['SP_Tim'])
        for i, results in enumerate (value):
            sumTim.append(value[i].loc['DS_Tim'])

        for index, gage in enumerate (springTim): # loop through each gage (223)

            allWaterYears = 0
            counter = 0
            year = int(gage.index[0])

            for i, flow in enumerate(gage): # loop through each year in the gage
                if is_nan(springTim[index][i]) == False and is_nan(sumTim[index][i]) == False:
                    allWaterYears = allWaterYears + 1
 
                    julianSpringTim = [int(springTim[index][i])]
                    offsetSpringTim = convertJulianToOffset(julianSpringTim, year)
                    julianSumTim = [int(sumTim[index][i])]
                    offsetSumTim = convertJulianToOffset(julianSumTim, year)

                    if offsetSpringTim[0] + 150 <= offsetSumTim[0]:
                        counter = counter + 1

            if currentClass in springBflLag:
                springBflLag[currentClass].append(counter/allWaterYears)
            else:
                springBflLag[currentClass] = [counter/allWaterYears]

    for currentClass in springBflLag:
        springBflLag[currentClass] = np.nanmean(springBflLag[currentClass])

    return springBflLag
