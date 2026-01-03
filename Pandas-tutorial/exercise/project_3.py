import pandas as pd
import numpy as np
dataset = pd.read_csv("..\\cvsfile\\project3_sales.csv")
# print(dataset)
def conver_to_datetime(df):
    new_df = pd.to_datetime(df,errors='coerce')
    return new_df
def add_revenue(quantity_df,price_df):
    revenue =quantity_df*price_df
    return revenue
def varify_dtypes(df):
    print("The Datatype of given Data frame")
    print(df.dtypes)
def sort_by_given_val(df,value):
    sorted_df = df.sort_values(value)
    return sorted_df
def month_filtering(df,col_name,month):
    month_filter = df[df[col_name].dt.month == month]
    return month_filter
def normal_filtering(df,col_name,value):
    filtered = df[df[col_name] == value]
    return filtered
def filter_by_range(df,col_name,start,end):
    range_filter = df[(df[col_name] >= start) & (df[col_name] <= end)]
    return range_filter
def reassembling(df,col_name1,col_name2,time,agg,roll_no=0,is_roll=False):
    if(is_roll):
        assembled = df.resample(time, on=col_name1)[col_name2].rolling(roll_no).mean()
        return assembled
    if(agg =='sum'):
        assembled = df.resample(time, on=col_name1)[col_name2].sum()
        return assembled
    if(agg =='mean'):
        assembled = df.resample(time, on=col_name1)[col_name2].mean()
        return assembled
def pivot_table(df,ind_col,col_col,val_col,agg):
    pivot = df.pivot_table(index = df[ind_col].dt.to_period('M'),
                           columns= col_col,
                           values= val_col,
                           aggfunc= agg)
    return pivot

dataset['date'] = conver_to_datetime(dataset['date'])
dataset['revenue'] = add_revenue(dataset['quantity'],dataset['price'])
varify_dtypes(dataset)
dataset = sort_by_given_val(dataset,'date')
jan_filter = month_filtering(dataset,'date',1)
electronic_filter = normal_filtering(dataset,'category','Electronics')
date_range_filter = filter_by_range(dataset,'date','2024-03-01','2024-04-15')
product_filter = normal_filtering(dataset,'product','Mouse B')
daily_revenue = reassembling(dataset,'date','revenue','D','sum',0,False)
monthly_revenue = reassembling(dataset,'date','revenue','ME','sum',0,False)
weekly_quantity = reassembling(dataset,'date','quantity','W','sum',0,False)
daily_avg_revenue = reassembling(dataset,'date','revenue','D','mean',0,False)
categpry_pivot = pivot_table(dataset,'date','category','revenue','sum')
daily_7 = reassembling(dataset,'date','revenue','D','mean',7,True)
daily_14 = reassembling(dataset,'date','revenue','D','mean',14,True)
daily_30 = reassembling(dataset,'date','revenue','D','mean',30,True)



print(categpry_pivot)
print(daily_7.head(15))
print(daily_14.head(20))
print(daily_30.head(35))
# print(daily_revenue)
# print(monthly_revenue)
# print(weekly_quantity)
# print(daily_avg_revenue)

# print(jan_filter)
# print(electronic_filter)
# print(date_range_filter)
# print(product_filter)
# print(dataset)
print(dataset.info())