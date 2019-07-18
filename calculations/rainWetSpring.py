import numpy as np
from Utils.convertDateType import convertJulianToOffset

def rainWetSpring(classes):
    rainWetSpring = {}
    for currentClass, value in classes.items():
        wetTim = []
        springTim = []

        for i, results in enumerate(value):
            springTim.append(value[i].loc['SP_Tim'])
        for i, results in enumerate(value):
            wetTim.append(value[i].loc['Wet_Tim'])

        for index, gage in enumerate(springTim): # loop through SP val's for each gage (223)
            counter = 0
            allWaterYears = 0
            year = int(gage.index[0])
            for i, flow in enumerate(gage): # loop through each year in the gage
                if np.isnan(wetTim[index][i]) == False and np.isnan(springTim[index][i]) == False:
                    allWaterYears = allWaterYears + 1

                    julianWetTim = [int(wetTim[index][i])]
                    offsetWetTim = convertJulianToOffset(julianWetTim, year)

                    julianSpringTim = [int(springTim[index][i])]
                    offsetSpringTim = convertJulianToOffset(julianSpringTim, year)
                    if offsetWetTim[0] + 30 >= offsetSpringTim[0]: # within 30 days each other
                        counter = counter + 1

            if currentClass in rainWetSpring:
                rainWetSpring[currentClass].append(counter/allWaterYears)
            else:
                rainWetSpring[currentClass] = [counter/allWaterYears]

    for currentClass in rainWetSpring:
        rainWetSpring[currentClass] = np.nanmean(rainWetSpring[currentClass])
    rainWetSpring['class1'] = None
    rainWetSpring['class9'] = None
    return rainWetSpring
