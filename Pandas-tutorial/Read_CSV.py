# Read_CSV

import pandas as pd

df = pd.read_csv(".\cvsfile\Employee_record.csv")
print(df.to_string()) 
# If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:

needf = pd.read_csv(".\cvsfile\data.csv")
print(needf)


# In my system the number is 60, which means that if the DataFrame contains more than 60 rows, 
# the print(df) statement will return only the headers and the first and last 5 rows.

print(pd.options.display.max_rows)

# increase the max row 
pd.options.display.max_rows = 9999

df = pd.read_csv(".\cvsfile\data.csv")

print(df) 