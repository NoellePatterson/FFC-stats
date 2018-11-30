import numpy as np

def wetCount(classes): 
    wetResult = {}
    
    for currentClass, value in classes.items():
        wetCount = []
        sumCount = []
        springCount = []
        # Create a list for each of the timing results across all gages
        for i, results in enumerate(value):
            wetCount.append(value[i].iloc[15,:])
            
        for i, results in enumerate(value):
            sumCount.append(value[i].iloc[7,:])
            
        for i, results in enumerate(value):
            springCount.append(value[i].iloc[3,:])
    
        for index, gage in enumerate(wetCount): # loop through each gage (223)
            allWaterYears = 0
            counter = 0
            for i, year in enumerate(gage): # loop through each year in the gage
                allWaterYears = allWaterYears + 1
                # check if winter timing isn't calculated when spring or summer are 
                if  np.isnan(year) and (not np.isnan(sumCount[index][i]) or not np.isnan(springCount[index][i])):
                    counter = counter + 1
                    
            if currentClass in wetResult:
                wetResult[currentClass].append(counter/allWaterYears)    
            else:
                wetResult[currentClass] = [counter/allWaterYears]
           
    for currentClass in wetResult: 
        wetResult[currentClass] = np.nanmean(wetResult[currentClass])                        
        
    return wetResult
 
