# analyzing data


# viewing data
# header() return the header and specified number of row
import pandas as pd
df = pd.read_csv(".\cvsfile\data.csv")
# print(df.head(20))

# head() along return first 5 rows

print(df.head())

# The tail() method returns the headers and a specified number of rows, starting from the bottom.

print(df.tail(10))
print(df.tail())# last 5 rows will return

# info() retuen the information about the data file
print(df.info()) 