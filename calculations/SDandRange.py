from Utils.calcSpreadMetrics import calcSpreadMetrics

def SDandRange(classes):
    SDwet, Wet10, Wet90, roc10, roc90 = calcSpreadMetrics(classes, 'Wet_Tim')
    SDspring, Spring10, Spring90, roc10, roc90 = calcSpreadMetrics(classes, 'SP_Tim')
    SDdry, Dry10, Dry90, roc10, roc90 = calcSpreadMetrics(classes, 'DS_Tim')

    return SDwet, Wet10, Wet90, SDspring, Spring10, Spring90, SDdry, Dry10, Dry90, roc10, roc90