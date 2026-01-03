# A Pandas DataFrame is a 2 dimensional data structure, 
# like a 2 dimensional array, or a table with rows and columns.

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": ["50", "40", 45]
}

#load data into a D
# ataFrame object:
df = pd.DataFrame(data)

print(df) 

# loc for returnning 1 or more specif row
#refer to the row index:
# print(df.loc[0]) #This example returns a Pandas Series.
print(df.loc[[1, 1]])
print(df.loc[[0, 1,2]])

# naming index
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)

#refer to the named index:
print(df.loc["day2"])

# load files into data frame
df = pd.read_csv("Pandas-tutorial\cvsfile\Employee_record.csv")
print(df) 