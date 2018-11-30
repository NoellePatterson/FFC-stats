import numpy as np

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
                allWaterYears = allWaterYears + 1
                if springTim[index][i] + 45 >= sumTim[index][i]:
                    counter = counter + 1
                    snowSpringBflRateArray.append(None)
                    snowSpringBflRateArray[-1] = value[index].loc['SP_ROC'][i] #index the rate of change years matching the sp-bfl criteria
                elif springTim[index][i] + 45 < sumTim[index][i]:
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

    return snowSpringBfl, snowSpringBflRate, allOtherYearsRate