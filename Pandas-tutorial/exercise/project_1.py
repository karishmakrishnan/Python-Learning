import pandas as pd
import numpy as np
messy_set = pd.read_csv("..\\cvsfile\\messy_employee_data.csv")
# print(messy_set)
# print(messy_set.head())
# print(messy_set.describe(include='all'))
#========================================================================================#
# Step----1
# 1. Removing the unwanted spaces
messy_set['name'] = messy_set['name'].str.strip()
messy_set['department'] = messy_set['department'].str.strip()
messy_set['email'] = messy_set['email'].str.strip()
messy_set['city'] = messy_set['city'].str.strip()
# 2. Standerdise the text
messy_set['name'] = messy_set['name'].str.title()
messy_set['department'] = messy_set['department'].str.title()
messy_set['email'] = messy_set['email'].str.lower()
messy_set['city'] = messy_set['city'].str.title()
# print(messy_set.to_string())
# Step-----2
# 1. Change the datatype
messy_set['age'] = messy_set['age'].str.strip()
messy_set['age'] = messy_set['age'].replace("thirty",30)
age_mode = messy_set['age'].mode()
messy_set['age'] = messy_set['age'].replace(np.nan,age_mode[0])
messy_set['age'] = messy_set['age'].astype(int)
# 2. cleaning salry
salary_mean = messy_set["salary"].mean(numeric_only=True)
messy_set['salary'] = messy_set['salary'].replace(np.nan,salary_mean)
# 3. Cleaning join date
messy_set['join_date'] = pd.to_datetime(messy_set['join_date'],dayfirst=True, errors='coerce')
messy_set['join_date'] = messy_set['join_date'].fillna(pd.Timestamp('1900-01-01'))
# 4. Remove duplicates
messy_set = messy_set.drop_duplicates(subset=['id'])
messy_set['id'] = messy_set['id'].replace(np.nan, 6)
# 5.Cleaning email,department, name
messy_set['email'] = messy_set['email'].fillna("unknow@example.com")
messy_set['department'] = messy_set['department'].fillna("Unknown")
messy_set['name'] = messy_set['name'].fillna("Unknown")
messy_set['city'] = messy_set['city'].fillna("Unknown")
#fix email
messy_set.loc[messy_set['email'] == 'bob@example', 'email'] = 'bob@example.com'
messy_set.loc[messy_set['email'] == 'wrong_email', 'email'] = 'unknown@example.com'
print(messy_set.to_string())
print(messy_set.info())
print(messy_set.isna().sum())
















