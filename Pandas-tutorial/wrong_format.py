# wrong format
# To fix it, you have two options: remove the rows, or 
# convert all cells in the columns into the same format.

import pandas as pd

df = pd.read_csv(".\cvsfile\sample2.csv")
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
df.dropna(subset=['Date'], inplace = True)#Remove rows with a NULL value in the "Date" column:
print(df)







