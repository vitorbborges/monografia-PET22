import pandas as pd
import os
import numpy as np

partial_folder = os.getcwd() + '\\journals-partial\\'
df=pd.DataFrame()

for i in os.listdir(partial_folder):
    dfp = pd.read_excel(partial_folder + i)
    df = pd.concat([df,dfp])
    
df.to_csv('journals.csv', index=False)