import math

# function works with list input
def convertOffsetToJulian(offsetDateList, year): # convert offset date to julian
    julianDateList = []
    for count, offsetDate in enumerate(offsetDateList):
        if year % 4 == 0:
            daysInYear = 366
            offsetStartDate = 274
        else:
            daysInYear = 365
            offsetStartDate = 273

        intOffsetDate = int(offsetDate)

        if intOffsetDate <=  offsetStartDate:
            julian_nonoffset_date = intOffsetDate + (daysInYear - offsetStartDate)
            julianDateList.append(julian_nonoffset_date)
        else:
            julian_nonoffset_date = intOffsetDate - offsetStartDate
            julianDateList.append(julian_nonoffset_date)

    return julianDateList

def convertOffsetToJulianSingle(offsetDate, year):
    if year % 4 == 0:
        daysInYear = 366
        offsetStartDate = 274
    else:
        daysInYear = 365
        offsetStartDate = 273
        intOffsetDate = int(offsetDate)
    if intOffsetDate - (daysInYear - offsetStartDate) > 0:
        julian_nonoffset_date = intOffsetDate - (daysInYear - offsetStartDate)
    else:
        julian_nonoffset_date = intOffsetDate + offsetStartDate
    return julian_nonoffset_date

# function works with list input
def convertJulianToOffset(julianDateList, year):
    offsetDateList = []
    for count, julianDate in enumerate(julianDateList):
        if year % 4 == 0:
            daysInYear = 366
            offsetStartDate = 274
        else:
            daysInYear = 365
            offsetStartDate = 273

        julianDate = int(julianDate)
        if math.isnan(julianDate) == False: 
            intJulianDate = int(julianDate)
            if intJulianDate >= offsetStartDate:
                offsetDate = intJulianDate - offsetStartDate
                offsetDateList.append(offsetDate)
            else:
                offsetDate = intJulianDate + (daysInYear - offsetStartDate)
                offsetDateList.append(offsetDate)
        else: offsetDate = julianDate

    return offsetDateList

# function works with single value input
def convertJulianToOffsetSingle(julianDate, year):
    if year % 4 == 0:
        daysInYear = 366
        offsetStartDate = 274
    else:
        daysInYear = 365
        offsetStartDate = 273

    julianDate = int(julianDate)
    if math.isnan(julianDate) == False: 
        intJulianDate = int(julianDate)
        if intJulianDate >= offsetStartDate:
            offsetDate = intJulianDate - offsetStartDate
        else:
            offsetDate = intJulianDate + (daysInYear - offsetStartDate)
    else: offsetDate = julianDate

    return offsetDate