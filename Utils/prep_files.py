import glob as glob
import pandas as pd
import os

path = 'Highflow-Results'

# select all files in each class folder
files = glob.glob(path+'/*_annual_result_matrix.csv')
# for each file, remove index column and rename: 11446220_class2_annual_result_matrix
for current_file in files:
    df = pd.read_csv(current_file, sep = ',', index_col=None)
    if df.columns.values[0] == 'Unnamed: 0':
        df = df.drop(columns=['Unnamed: 0'])
    df.to_csv('Highflow-Results2/'+current_file[21:], index=False)

