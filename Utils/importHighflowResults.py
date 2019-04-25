import pandas as pd

def importHighflowResults(files):
    classes = {}

    for i, file in enumerate(files):
        currentClass = 'class{}'.format(int(file[31]))
        currentFile = pd.read_csv(file, sep=',', dtype=str)
        currentFile.index = currentFile.iloc[:,0]
        currentFile.drop(['Year'], axis=1, inplace=True)
        if currentClass in classes:
            classes[currentClass].append(currentFile)
            continue
        classes[currentClass] = [currentFile]
    return classes

