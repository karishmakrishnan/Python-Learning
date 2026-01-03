import pandas as pd

df = pd.read_csv(".\cvsfile\sample2.csv")
df.loc[6, 'Duration'] = 45 #changing the data value by passing the index
print(df)

# changing the value by specifiying the condition
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

print(df)

# removing the value by checking wrong data
for x in df.index:
  if df.loc[x, "Duration"] > 90:
    df.drop(x, inplace = True)

print(df)
print(df.duplicated())

df.drop_duplicates(inplace = True) ##remove duplicate from the table
print(df)
# Remember: The (inplace = True) will make sure that the method does 
# NOT return a new DataFrame,
# but it will remove all duplicates from the original DataFrame.

# correlation
#corr()
print(df.corr())

# The Result of the corr() method is a table with a lot of numbers that represents how well the relationship is between two columns.
# The number varies from -1 to 1.
# 1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a value went up in the first column, the other one went up as well.
# 0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.
# -0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.
# 0.2 means NOT a good relationship, meaning that if one value goes up does not mean that the other will.

