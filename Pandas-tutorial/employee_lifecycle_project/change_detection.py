import pandas as pd
import numpy as np
import read_and_validate as rd #type:ignore

valid_df = rd.emp_clean.sort_values(["emp_id","update_ts"], ascending=[True,True])
valid_df["previous_salary"] = (
                            valid_df.groupby("emp_id")["salary"].shift(1)
)
conditions_sal = [valid_df["salary"] > valid_df["previous_salary"]]
choice_sal = ["CHANGED"]

condition_stat = [valid_df["previous_salary"].isna()]
choice_stat = ["YES"]
valid_df["salary_changed"] = np.select(conditions_sal, choice_sal, default="UNCHANGED")
valid_df["is_new"] = np.select(condition_stat,choice_stat, default="NO")

valid_df["start_date"] = valid_df["update_ts"]
valid_df["end_date"] = valid_df.groupby("emp_id")["update_ts"].shift(-1)
scd_df = valid_df[(valid_df["is_new"] == "YES") |(valid_df["salary_changed"] == "CHANGED")]
scd_df["is_current"] = np.where(scd_df["end_date"].isna(), "YES","NO")
# print(scd_df.loc[:,["emp_id", "name","dept", "salary", "start_date", "end_date","is_current"]].to_string())
emp_current = rd.latest_valid(scd_df[scd_df["is_current"] == "YES"])
print(emp_current.to_string())