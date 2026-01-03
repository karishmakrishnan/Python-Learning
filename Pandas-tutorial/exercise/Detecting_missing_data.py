import pandas as pd
import numpy as np

df = pd.read_csv(".\..\..\Pandas-tutorial\cvsfile\messy_dataset.csv")
# print(df)
# new_df = df.notna()
# print(df.isna())
# print(new_df)

# missing=df.isna().sum()
# print("nmissing : ")
# print(missing)
# print(missing['name'])

# total_missing = df.isna().sum().sum()
# print("Total Missing")
# print(total_missing)
# print(df.notna().sum())
# # print(df.count())
# print(df.info())

# new_df = df.dropna(subset=['name','salary'])
# print(df)
# print(new_df)
# new_df['join_date'].fillna(method = 'ffill')
# print("\n")
# # new_df['join_date'].bfill()
# new_df = new_df.fillna({'join_date': '2019-11-09'})
# mode = df['city'].mode()
# print(mode)
# print(new_df)
# new_df = new_df.fillna({'city': mode[0]})
# print("\n")
# print(new_df)
# print("\n")
# medien = df['age'].mode()
# new_df = new_df.fillna({'age': medien[0]})
# print(new_df)


# ###duplicate

print(df.duplicated())
print(df[df.duplicated])
df.drop_duplicates(inplace=True)
print(df)

df['name'] = df['name'].replace(r'\d+','',regex=True) # remove int from str
# df['join_date'] = df['join_date'].replace(r'^\\','\\',regex=True)
df['salary'] = df['salary'].replace('?',18000)
df['salary'] = df['salary'].replace([45000,50000],0)
df['city'] = df['city'].replace({
    'NY': 'New York'
})
df['age'] = df['age'].replace('?',18)
df['age'] = df['age'].replace('thirty',30)
df['age'] = df['age'].replace(np.nan,30)
df['salary'] = df['salary'].replace(np.nan,18000)
df["salary"] = df["salary"].replace({
    50000: 18000,
    45000: 18000
})
df["join_date"] = df["join_date"].ffill()
df['city'] = df['city'].replace(np.nan,"unknown")
df['name'] = df['name'].replace(np.nan,"unknown")

df['city'] = df['city'].str.upper()
df['name'] = df['name'].str.title()

df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce')
df["join_date"] = df["join_date"].ffill()
df['year'] = df['join_date'].dt.year
df['month'] = df['join_date'].dt.month
df['day'] = df['join_date'].dt.day
print(df)
print(df.info())
print(df.isna())
print(df.isna().sum())
new_df = df