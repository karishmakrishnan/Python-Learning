# cleaning data
# 1.cleaning empty cell
# Data cleaning means fixing bad data in your data set.

# Bad data could be:

# Empty cells
# Data in wrong format
# Wrong data
# Duplicates

# Remove rows
# One way to deal with empty cells is to remove rows that contain empty cells.
# This is usually OK, since data sets can be very big, 
# and removing a few rows will not have a big impact on the result.

import pandas as pd
# pd.rea
df = pd.read_csv(".\cvsfile\data.csv")

new_df = df.dropna() #dropna() creates a new csv file and removw the emptyrows
# print(df.info())
# print(new_df.info())

# print(new_df.to_string())

df_new = pd.read_csv(".\cvsfile\datacopy.csv")
df_new.dropna(inplace = True)

# print(df.to_string())

# print("============")
# print(df.info())
# print("============")
# print(df_new.info())
# print(df_new.to_string())



# Replace the empty values
# Replace Empty Values
# Another way of dealing with empty cells is to insert a new value instead.
# This way you do not have to delete entire rows just because of some empty cells.
# The fillna() method allows us to replace empty cells with a value:
df.fillna(130, inplace = True)
print(df.to_string())





