import pandas as pd
import numpy as np

emp_messy_data = pd.read_csv(".\\employee_daily.csv")
def casting_to_date(df,column):
    new_df = pd.to_datetime(df[column], errors="coerce")
    return new_df
def casting_to_string(df, column):
    new_series = df[column].astype("string")
    return new_series
def clean(df):
    latest_valid_df = df[(df["salary"] > 0) & (df["emp_id"].notna())]
    return latest_valid_df
def invalid():
    invalid_df = emp_messy_data
    invalid_df = invalid_df[invalid_df['emp_id'].isna()]
    sal_invalid  = emp_messy_data[emp_messy_data["salary"] <= 0]
    invalid_df = pd.concat([invalid_df, sal_invalid])
    # print(invalid_df.to_string())
    return invalid_df
def latest_valid(df):
    latest_valid_df = df
    latest_valid_df = df.sort_values(["emp_id", "update_ts"], ascending=[True,False])
    latest_valid_df["row_number"] = latest_valid_df.groupby("emp_id").cumcount()+1
    # latest_valid_df["row_number"] = latest_valid_df["row_number"].astype("Int64")
    # latest_valid_df = latest_valid_df[(latest_valid_df["salary"] > 0) & (latest_valid_df["emp_id"].notna())]
    latest_valid_df = latest_valid_df[latest_valid_df["row_number"] == 1].drop(columns=["row_number"])
    return latest_valid_df

emp_messy_data["update_ts"] = casting_to_date(emp_messy_data, "update_ts")
emp_messy_data["dept"] = casting_to_string(emp_messy_data, "dept")
emp_messy_data["name"] = casting_to_string(emp_messy_data, "name")
emp_clean = clean(emp_messy_data)
emp_latest = latest_valid(emp_clean)
invalid_df = invalid()
# print(invalid_df.to_string())