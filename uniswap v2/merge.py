import os,sys
import pandas as pd
import glob

csv_list = glob.glob('*.csv')
print(u'find %s CSV files'% len(csv_list))
for i in csv_list:
    fr = open(i,'rb').read()
    with open('result10.csv','ab') as f:
        f.write(fr)
