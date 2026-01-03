
# A Pandas Series is like a column in a table.
# It is a one-dimensional array holding data of any type.
import pandas as pd

a = (1, 7, 2)
myvar = pd.Series(a)
print(myvar)
print(myvar[0])

# Labels
# If nothing else is specified, the values are labeled with their index number.
# First value has index 0, second value has index 1 etc.
# This label can be used to access a specified value.

# using index argument to label each value
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
print(myvar['x'])
print(myvar['y'])
print(myvar['z'])

# Using dictionary (key /value) for series and key is label when we do that

calories = {"day1": 40, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
print(myvar['day1'])
print(myvar['day2'])
print(myvar['day3'])

# using index to assign few values to series
myvar = pd.Series(calories, index = ["day", "day2667"])
print(myvar.shape)
print(myvar)



# DataFrames
# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)
print(myvar['calories'])
print(myvar['calories'][0]) #access the list items
print(myvar['duration'])
print(myvar['duration'][2]) #access the list items