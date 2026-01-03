import pandas as pd
import numpy as np
data = {
"emp_id": [101,102,103,104,105,106,107],
"name": ["Asha","Ravi","John","Meena","Kiran","Priya","Arun"],
"dept": ["IT","HR","IT","Finance","HR","IT","Finance"],
"salary": [70000,50000,80000,60000,52000,75000,65000],
"join_date": ["2021-01-10","2020-03-15","2019-07-01","2022-02-20","2021-06-18","2018-11-05","2020-09-12"],
"location": ["Bangalore","Chennai","Bangalore","Mumbai","Chennai","Bangalore","Mumbai"]
}

df = pd.DataFrame(data)
print(df.shape)
# print(df['location'] == 'Bangalore')
# print(df[df['location'] == True])
# print(df)
df['join_date'] = pd.to_datetime(df["join_date"])

# 1 Employees from IT department with salary > 72000
# 2 Employees from Chennai OR Mumbai
# 3 Employees who joined after 2020

first_filter = df[(df['dept'] == 'IT') & (df['salary'] > 72000)]
city_filter = df[(df['location'] == 'Chennai') | (df["location"] == 'Mumbai')]
year_filter = df[df["join_date"].dt.year > 2020]

print(first_filter)
print("===============================================")
print(city_filter)
print("===============================================")
print(year_filter)
print("===============================================")

# 1 Create salary_band: High / Medium / Low
# 2 Create join_year column
# for x in df:
#     # if df["salary"] > 75000:
#     #     df['salary_band'] = "HIGH"
#     # elif df["salary"].between(6000,75000):
#     #     df["salary_band"] = "MEDIUM"
#     # elif df["salary"] < 60000:
#     #     df["salary_band"] = "LOW"
    # print(x)

# df['salary_band'] = "HIGH" if df["salary"] > 75000 else "MEDIUM" if (df["salary"].between(6000,75000)) else "LOW"
conditions = [df["salary"] > 75000, df["salary"].between(60000,75000)]
choices = ["HIGH", "MEDIUM"]
df["salary_band"] = np.select(conditions,choices, default="LOW")
df['join_year'] = df["join_date"].dt.year
print(df)
print("===============================================")
# 1 Average salary per department
# 2 Employee count per location
# 3 Department-wise max and min salary

avg_sal_dept = df.groupby("dept")['salary'].mean()
emp_loc_count = df.groupby("location")["emp_id"].count()
dept_min_salary = df.groupby("dept")['salary'].min()
dept_max_salary = df.groupby("dept")['salary'].max()

dept_salary_stats = (
    df.groupby("dept").agg(
        avg_sal = ("salary", "mean"),
        min_sal = ("salary", "min"),
        max_sal = ("salary", "max")
    )
)
print(dept_salary_stats)
print(avg_sal_dept)
print("===============================================")
print(emp_loc_count)
print("===============================================")
print(dept_min_salary)
print("===============================================")
print(dept_max_salary)
print("===============================================")

# 1 Sort employees by salary descending
# 2 Rank employees by salary within department
# Exercise 5: Missing Data
# df.loc[2, "salary"] = None
# df.loc[5, "location"] = None
# 1 Identify missing values
# 2 Fill missing salary with department average
# 3 Fill missing location with 'Unknown'

rank_emp_sal = df.groupby('dept')['salary'].rank(ascending=False)

sort_df = df.sort_values(by="salary", ascending=False)
df.loc[2, "salary"] = None
df.loc[5, "location"] = None
df.loc[2, "salary"] = None

print(rank_emp_sal)
print("===============================================")
print(sort_df)
print("===============================================")

df['salary'] = df['salary'].fillna(
    df.groupby('dept')['salary'].transform('mean')
)
df["location"] = df["location"].fillna("UNKNOWN")

print(df)