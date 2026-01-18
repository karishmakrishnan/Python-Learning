import pandas as pd
import numpy as np
import sys
data = [1, None, 2, None, 3, 4, None]

cleaned_data = [x for x in data if x is not None]
print(cleaned_data)

replace_with_zero = [x if x is not None else 0 for x in data]
print(replace_with_zero)

mean = sum([x for x in data if x is not None])/len([x for x in data if x is not None])
replace_with_mean = [x if x is not None else mean for x in data]
print(replace_with_mean)

data = {
'A': [1, 2, np.nan, 4, 5],
'B': [np.nan, 2, 3, np.nan, 5],
'C': [1, np.nan, np.nan, 4, 5]
}
df = pd.DataFrame(data)

print(df.isna()) # we can use isnull() also to detect nan

# REMOVING THE MISSING VALUES
cleaned_row = df.dropna() #drop row which has nan
print(cleaned_row)
cleaned_column = df.dropna(axis=1) #drop column which has nan
print(cleaned_column)
cleaned_df = df.dropna(how="any") # remove rows where any value is missing/nan
print(cleaned_df)
cleaned_df =df.dropna(how="all") # removes rows where all values are missing/nan
print(cleaned_df)
cleaned_df = df.dropna(subset=['A'])  #from column A missing value is removed
print(cleaned_df)

# REPLACING THE MISSING VALUES
value_replace = df.fillna(0)
print(value_replace)
mean_replace = df.fillna(df.mean())
print(mean_replace)
ffill_replace = df.ffill()
print(ffill_replace)
bfill_replace = df.bfill()
print(bfill_replace)
interpolated_df = df.interpolate()
print(interpolated_df)
print(sys.getrefcount(df))

def print_args(*args):
    for arg in args:
        print(arg)
print_args(1,2,3)

def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_kwargs(name="Alice",age=30,city="NewYork")

def print_args_kwargs(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
print_args_kwargs(1, 2, 3, name="Alice", age=30)

def wrapper_function(func, *args, **kwargs):
    print("Wrapper function called")
    return func(*args, **kwargs)
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
result = wrapper_function(greet, "Alice", greeting="Hi")
print(result) 