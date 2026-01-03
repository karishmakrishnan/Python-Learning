import pandas as pd
import numpy as np
# import Detecting_missing_data as dm

df = pd.read_csv(".\..\..\Pandas-tutorial\cvsfile\messy_dataset.csv")
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

# ==================================

# print(df[df['age']>30])
print(df.info())
df['age'] = df['age'].astype(int)
print(df.info())
print(df[df['age']>30])
print(df[(df['age'] > 20)& (df['city'] == 'NEW YORK')])

df['salary'] = df['salary'].astype(float)
print(df[df['salary'] == 18000])
print(df[(df['salary'] > 18000)& (df['city'] == 'CHICAGO')])


print(df[~df['name'].isna()])

new_city_df = df[df['city'].isin(['NEW YORK','CHICAGO'])]
print(new_city_df)

salary_filter = df[df['salary'].between(45000,90000)]
print(salary_filter)

age_filter = df[df['age'].between(35,60)]
print(age_filter)

salary_filter = df.query("(salary > 45000) and city == 'CHICAGO'")
print(salary_filter)

age_limit = 33
print(df.query("age > @age_limit"))
print(df.query("city not in['UNKNOWN']"))
print(df.query("city == 'UNKNOWN'"))

