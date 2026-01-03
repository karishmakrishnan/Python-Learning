import pandas as pd

data1 = {
    'ID':[1,2,3,4,5,6],
    'name': ['Anjali','Arathi', 'martha','Shamala','krishna','Karthic']
}
data2 = {
    'ID':[6,9,11],
    'name': ['Jaya','Kantha', 'june'],
    'score':[90,96,69]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

merge1 = df1.merge(df2,on='ID', how='outer')
merge2 = df1.merge(df2,how='cross')
print(df1)
print(df2)
print(merge2)

pd.melt(data2,id_vars='name',value_vars=['ID','Score'], var_name='rollnumber',value_name='score')
print(data2)









