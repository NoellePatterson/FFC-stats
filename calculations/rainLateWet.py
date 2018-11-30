from Utils.convertDateType import convertOffsetToJulian
import numpy as np

def rainLateWet(highflowClasses):
    rainLateWet = {}
    for currentClass, value in highflowClasses.items():
        wetTim = []

        percentiles = [2,5,10,20]
        highflow2 = []
        highflow5 = []
        highflow10 = []
        highflow20 = []
        for i, results in enumerate(value):
            wetTim.append(value[i].loc['FAFL_Tim_Wet']) # obtain date of wet timing each year
            for index, percentile in enumerate(percentiles): # also obtain highflow results
                if percentile == 2:
                    highflow2.append(value[i].loc['WIN_Tim_2'])
                if percentile == 5:
                    highflow5.append(value[i].loc['WIN_Tim_5'])
                if percentile == 10:
                    highflow10.append(value[i].loc['WIN_Tim_10'])
                if percentile == 20:
                    highflow20.append(value[i].loc['WIN_Tim_20'])

        ''''Try metric only with specific highflow percentiles'''

        for index, highflows in enumerate(highflow5): # loop through each gage
            highflowsEachYear = []
            year = int(highflows.index[0])
            highflowslist = highflows.tolist()
            annualResultsArray = [] # take average of subannual results to get value for each year
            for yearCount, highflow in enumerate(highflowslist): # loop through the years of each gage

                if highflow == '-99999' or highflow == 'None':
                    highflow = np.nan
                    highflowsEachYear.append(highflow)
                else:
                    if len(highflow) % 3 == 1:
                        highflow = '0' + highflow
                    elif len(highflow) % 3 == 2:
                        highflow = '00' + highflow
                    highflow = [highflow[i:i+3] for i in range(0, len(highflow), 3)]
                    highflow = convertOffsetToJulian(highflow, year)
                    for ct, val in enumerate(highflow):
                        highflow[ct] = float(val)
                    highflowsEachYear.append(highflow)
            subAnnualResultsArray = [] # save each year's results into an array
            for count, highflowEvents in enumerate(highflowsEachYear): # loop through each year in gage
                counter = 0
                allHighFlows = 0
                if type(highflowEvents) == list:
                    if type(wetTim[index][count]) == str:
                        for ii in range(0, len(highflowEvents)): # loop through each highflow event (if more than one in year)
                            allHighFlows = allHighFlows + 1
                            offsetWetTim = [int(float(wetTim[index][count]))]
                            julianWetTim = convertOffsetToJulian(offsetWetTim, year)
                            if highflowEvents[ii] < float(julianWetTim[0]):
                                counter = counter + 1
                        subAnnualResultsArray.append(None)
                        subAnnualResultsArray[-1] = counter/allHighFlows # array of results for each year, here
                annualResultsArray.append(None)
                annualResultsArray[-1] = np.nanmean(subAnnualResultsArray)
                # print(currentClass,     index,    count,    annualResultsArray)

            if currentClass in rainLateWet:
                    rainLateWet[currentClass].append(np.nanmean(annualResultsArray))
            else:
                rainLateWet[currentClass] = [np.nanmean(annualResultsArray)]

    for currentClass in rainLateWet:
        rainLateWet[currentClass] = np.nanmean(rainLateWet[currentClass])

    return rainLateWet
