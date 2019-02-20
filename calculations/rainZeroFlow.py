import numpy as np

def rainZeroFlow(classes):
    rainZeroFlow = {}
    for currentClass, value in classes.items():
        zeroFlow = []
        for index, results in enumerate(value): # loop through each gage (223)
            zeroFlow.append(np.nanmean(value[index].loc['DS_No_Flow'])) # list with the mean zero-flow days for each gage in the class
            if currentClass in rainZeroFlow:
                rainZeroFlow[currentClass].append(zeroFlow)    
            else:
                rainZeroFlow[currentClass] = [zeroFlow]   
    for currentClass in rainZeroFlow: 
        rainZeroFlow[currentClass] = np.nanmedian(rainZeroFlow[currentClass])
    rainZeroFlow['class1'] = None
    rainZeroFlow['class2'] = None
    rainZeroFlow['class3'] = None
    rainZeroFlow['class5'] = None
    rainZeroFlow['class9'] = None
        
    return rainZeroFlow
    

