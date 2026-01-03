import pandas as pd

df = pd.read_csv(".\cvsfile\sample2.csv")
# print(df.to_string())
new_df = df.dropna()
# print(new_df)

# df.dropna(inplace=True) #drop null row from orginal file
# df.dropna(130,inplace=True)# replace all nan with 130
# Replace Only For Specified Columns

# df.fillna({"Calories": 130}, inplace=True) #replacing value on specified column
print(df.to_string())

x = df["Calories"].mean()#sum of total values divided by total number

df.fillna({"Calories": x}, inplace=True)
# print(df)

y = df["Maxpulse"].median() #value in the middle after sorting
df.fillna({"Maxpulse": y}, inplace=True)
# print(df)

z = df["Pulse"].mode()[0]#the value that appears most frequently.
df.fillna({"Pulse": z}, inplace=True)
# print(df)

df.fillna(120,inplace=True)
print(df)