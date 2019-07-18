from Utils.convertDateType import convertJulianToOffset
import numpy as np
import math

def is_nan(x):
    return (x is np.nan or x != x)

def rainEarlySpring(classes):
    rainEarlySpring = {}
    for currentClass, value in classes.items(): # loop through each class
        springTim = []

        percentiles = [2,5,10,20]
        highflow2_upper = []
        highflow5_upper = []
        highflow10_upper = []
        highflow20_upper = []
        for i, results in enumerate(value): # loop through each gage
            springTim.append(value[i].loc['SP_Tim']) # obtain date of sp recession each year
            for index, percentile in enumerate(percentiles): # also obtain highflow results
                if percentile == 2:
                    highflow2_upper.append(value[i].loc['Peak_Dur_2'])
                elif percentile == 5:
                    highflow5_upper.append(value[i].loc['Peak_Dur_5'])
                elif percentile == 10:
                    highflow10_upper.append(value[i].loc['Peak_Dur_10'])
                elif percentile == 20:
                    highflow20_upper.append(value[i].loc['Peak_Dur_20'])

        ''''Try metric only with specific highflow percentiles'''
        counter = 0
        annualResultsArray = []
        for index, gage in enumerate(highflow5_upper): # loop through each gage
            for year, highflow in enumerate(gage): # loop through each year in the gage

                if is_nan(springTim[index][year]) == False:
                    julianSpringTim = [int(springTim[index][year])]
                    offsetSpringTim = convertJulianToOffset(julianSpringTim, year)
                    if highflow > float(offsetSpringTim[0]):
                        counter = counter + 1
                        # if currentClass == 'class5':
                        #     print('year' + str(year) + '_highflow' + str(highflow) + '_SpTim'+str(offsetSpringTim[0]))
        all_year_list = [item for sublist in highflow5_upper for item in sublist]
        metric = counter/len(all_year_list)
        if currentClass in rainEarlySpring:
            rainEarlySpring[currentClass].append(metric)
        else:
            rainEarlySpring[currentClass] = [metric]
    for currentClass in rainEarlySpring:
        rainEarlySpring[currentClass] = np.nanmean(rainEarlySpring[currentClass])
    rainEarlySpring['class1'] = None
    rainEarlySpring['class9'] = None
    return rainEarlySpring
