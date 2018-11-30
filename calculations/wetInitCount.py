import numpy as np

def wetInitCount(classes):    
    wetInitCount = {}
    for currentClass, value in classes.items():
        fallTim = []
        for i, results in enumerate (value):
            fallTim.append(value[i].iloc[13,:])
    
        for i, gage in enumerate (fallTim): # loop through each gage (223)
            allWaterYears = 0
            wetInitCounter = 0
            for i, year in enumerate(gage): # loop through each year in the gage
                allWaterYears = allWaterYears + 1
                if  year == 274:
                    wetInitCounter = wetInitCounter + 1
                    
                    
                    
            if currentClass in wetInitCount:
                wetInitCount[currentClass].append(wetInitCounter/allWaterYears)    
            else:
                wetInitCount[currentClass] = [wetInitCounter/allWaterYears]
      
    for currentClass in wetInitCount: 
        wetInitCount[currentClass] = np.nanmean(wetInitCount[currentClass]) 

    return wetInitCount
            