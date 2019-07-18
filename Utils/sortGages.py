import pandas as pd

def sortGages(files):
    classes = {}

    for i, file in enumerate(files):
        if len(file) == 56: # for files from All-results folder
            currentClass = 'class{}'.format(int(file[26:-25]))
        elif len(file) == 57: # for files from Highflow-results folder
            currentClass = 'class{}'.format(int(file[30:-25]))
        currentFile = pd.read_csv(file, sep=',')
        currentFile.index = currentFile.iloc[:,0]
        currentFile.drop(['Year'], axis=1, inplace=True)
        if currentClass in classes:
            classes[currentClass].append(currentFile)
            continue
        classes[currentClass] = [currentFile]
    return classes             
