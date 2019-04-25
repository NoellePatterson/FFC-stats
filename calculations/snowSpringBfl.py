import numpy as np
from Utils.convertDateType import convertJulianToOffset

def is_nan(x):
    return (x is np.nan or x != x)

def snowSpringBfl(classes): 
    snowSpringBfl = {}
    snowSpringBflRate = {}
    allOtherYearsRate = {}
    for currentClass, value in classes.items():
        springTim = []
        sumTim = []
        for i, results in enumerate(value):
            springTim.append(value[i].loc['SP_Tim'])
        
        for i, results in enumerate(value):
            sumTim.append(value[i].loc['DS_Tim'])
            
        counter = 0
        allWaterYears = 0
        snowSpringBflRateArray = []
        allOtherYearsRateArray = []
        for index, gage in enumerate(springTim): # loop through each gage (223)
            for i, year in enumerate(gage): # loop through each year in the gage
                if is_nan(springTim[index][i]) == False and is_nan(sumTim[index][i]) == False:
                    allWaterYears = allWaterYears + 1
                    julianSpringTim = [springTim[index][i]]
                    offsetSpringTim = convertJulianToOffset(julianSpringTim, year)
                    julianSumTim = [sumTim[index][i]]
                    offsetSumTim = convertJulianToOffset(julianSumTim, year)
                    if offsetSpringTim[0] + 45 >= offsetSumTim[0]:
                        counter = counter + 1
                        snowSpringBflRateArray.append(None)
                        snowSpringBflRateArray[-1] = value[index].loc['SP_ROC'][i] #index the rate of change years matching the sp-bfl criteria
                    elif offsetSpringTim[0] + 45 < offsetSumTim[0]:
                        allOtherYearsRateArray.append(None)
                        allOtherYearsRateArray[-1] = value[index].loc['SP_ROC'][i] #index the rate of change of all other years
                    
            if currentClass in snowSpringBfl:
                snowSpringBfl[currentClass].append(counter/allWaterYears) 
                snowSpringBflRate[currentClass].append(np.nanmean(snowSpringBflRateArray))
                allOtherYearsRate[currentClass].append(np.nanmean(allOtherYearsRateArray))
            else:
                snowSpringBfl[currentClass] = [counter/allWaterYears]
                snowSpringBflRate[currentClass] = [np.nanmean(snowSpringBflRateArray)]
                allOtherYearsRate[currentClass] = [np.nanmean(allOtherYearsRateArray)] 
      
    for currentClass in snowSpringBfl: 
        snowSpringBfl[currentClass] = np.nanmean(snowSpringBfl[currentClass])
        snowSpringBflRate[currentClass] = np.nanmean(snowSpringBflRate[currentClass])
        allOtherYearsRate[currentClass] = np.nanmean(allOtherYearsRate[currentClass])
    """Remove outputs for all classes besides snow"""
    snow_dicts = [snowSpringBfl, snowSpringBflRate, allOtherYearsRate]
    for snow_dict in snow_dicts:
        snow_dict['class3'] = None
        snow_dict['class4'] = None
        snow_dict['class5'] = None
        snow_dict['class6'] = None
        snow_dict['class7'] = None
        snow_dict['class8'] = None

    return snowSpringBfl, snowSpringBflRate, allOtherYearsRate