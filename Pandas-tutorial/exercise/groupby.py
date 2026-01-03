import pandas as pd
import numpy as np
# import Detecting_missing_data as dm

df = pd.read_csv(".\\Pandas-tutorial\cvsfile\messy_dataset.csv")
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


#===========================================
df['age'] = df['age'].astype(int)
df['salary'] = df['salary'].astype(float)

city_salary = df.groupby('city')['salary'].mean()
date_age = df.groupby(['join_date','age'])['salary'].count()
city_salary_agg = df.groupby('city')['salary'].agg(['mean','sum','count'])

city_salary.reset_index()

print(city_salary.keys())
print(city_salary)
print(city_salary)
print(date_age.reset_index())
# print(date_age.keys())
# print(city_salary_agg.keys())

for x in date_age:
    print("Groups :", x)
    print(date_age)
# city_salary.get("NEW YORK")