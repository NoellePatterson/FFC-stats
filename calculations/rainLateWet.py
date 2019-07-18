from Utils.convertDateType import convertJulianToOffset
import numpy as np
import math

def is_nan(x):
    return (x is np.nan or x != x)

def rainLateWet(highflowClasses):
    rainLateWet = {}
    for currentClass, value in highflowClasses.items():
        wetTim = []

        percentiles = [2,5,10,20]
        highflow2_lower = []
        highflow5_lower = []
        highflow10_lower = []
        highflow20_lower = []
        for i, results in enumerate(value):
            wetTim.append(value[i].loc['Wet_Tim']) # obtain date of wet timing each year
            for index, percentile in enumerate(percentiles): # also obtain highflow results
                if percentile == 2:
                    highflow2_lower.append(value[i].loc['Peak_Tim_2'])
                if percentile == 5:
                    highflow5_lower.append(value[i].loc['Peak_Tim_5'])
                if percentile == 10:
                    highflow10_lower.append(value[i].loc['Peak_Tim_10'])
                if percentile == 20:
                    highflow20_lower.append(value[i].loc['Peak_Tim_20'])

        ''''Try metric only with specific highflow percentiles'''
        counter = 0
        annualResultsArray = []
        for index, gage in enumerate(highflow5_lower): # loop through each gage
            for year, highflow in enumerate(gage): # loop through each year in the gage
                if is_nan(wetTim[index][year]) == False:
                    julianwetTim = [int(wetTim[index][year])]
                    offsetwetTim = convertJulianToOffset(julianwetTim, year)
                    if highflow < float(offsetwetTim[0]):
                        counter = counter + 1
                        # if currentClass == 'class5':
                        #     print('year' + str(year) + '_highflow' + str(highflow) + '_SpTim'+str(offsetSpringTim[0]))
        all_year_list = [item for sublist in highflow5_lower for item in sublist]
        metric = counter/len(all_year_list)
        if currentClass in rainLateWet:
            rainLateWet[currentClass].append(metric)
        else:
            rainLateWet[currentClass] = [metric]
    for currentClass in rainLateWet:
        rainLateWet[currentClass] = np.nanmean(rainLateWet[currentClass])
    rainLateWet['class1'] = None
    rainLateWet['class2'] = None
    rainLateWet['class3'] = None
    rainLateWet['class5'] = None
    rainLateWet['class9'] = None
    return rainLateWet