import numpy as np
from Utils.convertDateType import convertOffsetToJulian, convertJulianToOffset

def LSRspringBfl(classes):
    lagtime = 21
    LSRspringBfl = {}
    LSRspringBflRate = {}
    allOtherYearsRate = {}
    for currentClass, value in classes.items():
        springTim = []
        sumTim = []
        for i, results in enumerate(value):
            springTim.append(value[i].loc['SP_Tim'])

        for i, results in enumerate(value):
            sumTim.append(value[i].loc['DS_Tim'])

        allWaterYears = 0
        counter = 0
        LSRspringBflRateArray = []
        allOtherYearsRateArray = []
        for index, gage in enumerate(springTim): # loop through each gage (223)
            year = int(gage.index[0])
            for i, year in enumerate(gage): # loop through each year in the gage
                allWaterYears = allWaterYears + 1
                if np.isnan(springTim[index][i]) == False and np.isnan(sumTim[index][i]) == False:
                    julianSpringTim = [int(springTim[index][i])]
                    offsetSpringTim = convertJulianToOffset(julianSpringTim, year)

                    julianSumTim = [int(sumTim[index][i])]
                    offsetSumTim = convertJulianToOffset(julianSumTim, year)
                    if offsetSpringTim[0] + lagtime >= offsetSumTim[0]: # check when spring and summer are within 30 days of eachother
                        counter = counter + 1
                        LSRspringBflRateArray.append(None)
                        LSRspringBflRateArray[-1] = value[index].loc['SP_ROC'][i] # index the rate of change of that gage in that year
                    elif offsetSpringTim[0] + lagtime < offsetSumTim[0]:
                        allOtherYearsRateArray.append(None)
                        allOtherYearsRateArray[-1] = value[index].loc['SP_ROC'][i] #index the rate of change of all other years

            if currentClass in LSRspringBfl:
                LSRspringBfl[currentClass].append(counter/allWaterYears)
                LSRspringBflRate[currentClass].append(np.nanmean(LSRspringBflRateArray))
                allOtherYearsRate[currentClass].append(np.nanmean(allOtherYearsRateArray))
            else:
                LSRspringBfl[currentClass] = [counter/allWaterYears]
                LSRspringBflRate[currentClass] = [np.nanmean(LSRspringBflRateArray)]
                allOtherYearsRate[currentClass] = [np.nanmean(allOtherYearsRateArray)]

    for currentClass in LSRspringBfl:
        LSRspringBfl[currentClass] = np.nanmean(LSRspringBfl[currentClass])
        LSRspringBflRate[currentClass] = np.nanmean(LSRspringBflRate[currentClass])
        allOtherYearsRate[currentClass] = np.nanmean(allOtherYearsRate[currentClass])
    """Remove output values for all classes except LSR"""
    lsr_dicts = [LSRspringBfl, LSRspringBflRate, allOtherYearsRate]
    for lsr_dict in lsr_dicts:
        lsr_dict['class1'] = None
        lsr_dict['class4'] = None
        lsr_dict['class6'] = None
        lsr_dict['class7'] = None
        lsr_dict['class8'] = None
        lsr_dict['class9'] = None

    return LSRspringBfl, LSRspringBflRate, allOtherYearsRate
