import glob
import pandas as pd

# bring in all new files
new_files = glob.glob('All-Results/*_annual_result_matrix.csv')
# bring in all old files
old_files = glob.glob('Highflow-Results/*_annual_result_matrix.csv')
# go through each new file, find old file corresponds
for index, new_file in enumerate(new_files):
    
    new_gage = new_file[16:24]
    new_df = pd.read_csv(new_file, sep = ',')
    for index, old_file in enumerate(old_files):
        
        old_gage = old_file[17:25]
        if old_gage == new_gage:
            old_df = pd.read_csv(old_file, sep = ',')
            break
    old_df = pd.read_csv(old_files[index], sep = ',')
# match up old row and new row, insert old row into new row.
# make sure new name of row is retained
    new_df.iloc[18] = old_df.iloc[18]
    new_df.iloc[18,0] = 'Peak_Tim_2'
    new_df.iloc[22] = old_df.iloc[22]
    new_df.iloc[22,0] = 'Peak_Tim_5'
    new_df.iloc[26] = old_df.iloc[26]
    new_df.iloc[26,0] = 'Peak_Tim_10'
    new_df.iloc[30] = old_df.iloc[30]
    new_df.iloc[30,0] = 'Peak_Tim_20'
# check if old row and new row are same length. If not, we have a problem. 
    if len(new_df.iloc[18]) != len(old_df.iloc[18]):
        print('oh no!!!')
# export out successful results! 
    new_df.to_csv('Highflow-Results2/'+new_file[12:])
# import pdb; pdb.set_trace()