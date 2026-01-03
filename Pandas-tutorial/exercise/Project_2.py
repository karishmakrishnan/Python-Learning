import pandas as pd
import numpy as np

customer_dataset = pd.read_csv("..\\cvsfile\\customers.csv")
orders_dataset = pd.read_csv("..\\cvsfile\\orders.csv")
product_dataset = pd.read_csv("..\\cvsfile\\products.csv")

def CheckNAN(Dataset):
    print(Dataset.isnull().sum())
def CheckForDuplicates(Dataset):
    duplicates = Dataset.duplicated().sum()
    print("Duplicates: ")
    print(duplicates)
def CheckDataType(Dataset):
    datatype = Dataset.dtypes
    print("The data type is ",datatype)
def VailidateDate(Dataset):
    datetime = pd.to_datetime(Dataset, dayfirst=False, errors='coerce')
    return datetime
def MergeDataframe(df1,df2,common_col):
    df1_df2 = df1.merge(df2, on=common_col, how='left')
    return df1_df2
def extract_month(df):
    month = df.dt.month
    return month
def extrcat_year(df):
    year = df.dt.year
    return year
# ========================================================================================================
customer_dataset['signup_date'] = VailidateDate(customer_dataset["signup_date"])
orders_dataset['order_date'] = VailidateDate(orders_dataset["order_date"])
customer_order = MergeDataframe(customer_dataset,orders_dataset,'customer_id')
full_dataset = MergeDataframe(customer_order,product_dataset,'product_id')
full_dataset['revenue'] = full_dataset['price']*full_dataset['quantity']
full_dataset['month'] = full_dataset['order_date'].dt.month
full_dataset['year'] = full_dataset['order_date'].dt.year
print(full_dataset[['product_id','price','quantity','revenue']].head())
Total_revenue = full_dataset['revenue'].sum()
print("Total Revenue is: ", Total_revenue)
# ========================================================================================================
category_revenvue = full_dataset.groupby('category')['revenue'].sum().sort_values(ascending=False)
customer_revenue = full_dataset.groupby('customer_id')['revenue'].sum().sort_values(ascending=False).head(10)
city_revenue = full_dataset.groupby('city')['revenue'].sum().sort_values(ascending=False)
month_revenue = full_dataset.groupby('month')['revenue'].sum()
year_month_revenue = full_dataset.groupby(['month','year'])['revenue'].sum().sort_values(ascending=False).head(12)

full_dataset['signup_year'] = extrcat_year(full_dataset['signup_date'])

# ========================================================================================================
# level---1
product_revenue = full_dataset.groupby('product_id')['revenue'].sum()
total_quantity_of_category = full_dataset.groupby('category')['quantity'].sum().sort_values(ascending=False)
revenue_of_signup_ofcustomer = full_dataset.groupby(['signup_year'])['revenue'].sum()
orderd_per_customer = full_dataset.groupby('customer_id')['order_id'].sum()
per_city_per_year_revenue = full_dataset.groupby(['city','year'])['revenue'].sum()
# highest_revenue_of_category = full_dataset.groupby('category')['revenue'].sum().head(1)
order_avg_revenue = full_dataset.groupby(['order_id','category'])['revenue'].mean()
highest = category_revenvue.max()
category_revenvue_category = category_revenvue[category_revenvue == highest].index
print(f"highest categoty has revenue is: {highest} and category is {category_revenvue_category}")








# print(category_revenvue)
# print(customer_revenue)
# print(city_revenue)
# print(month_revenue)
# print(year_month_revenue)
# print(full_dataset.info())
# print(customer_order)
# print(full_dataset)
# print(full_dataset.info())
# print(full_dataset.head())
# print(orders_dataset.info())