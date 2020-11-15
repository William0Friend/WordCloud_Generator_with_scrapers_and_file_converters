import pandas as pd 
df = pd.read_fwf('wc_test.txt')
df.to_csv('wc_test.csv')