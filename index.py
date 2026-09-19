import numpy as np 
import pandas as pd 


data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 42],
    'City': ['New York', 'Paris', 'Berlin', 'London'],
    'Salary': [65000, 70000, 62000, 85000]
}
df = pd.DataFrame(data)
print(df)

data_list = [
    ['John', 28, 'New York', 65000],
    ['Anna', 34, 'Paris', 70000],
    ['Peter', 29, 'Berlin', 62000],
    ['Linda', 42, 'London', 85000]
]
df2 = pd.DataFrame(data_list)
columns = ["Name","Age","City","Salary"]
df2 = pd.DataFrame(data_list,columns =columns)
print(df2)

print(df2[["Name","City"]])

df2["Designation"] = ["Doctor","Eng.","Doctor","Eng."]
print(df2)
df2.drop(0,axis = 0)
print(df2)

df2.loc[[0,1]]

df.iloc[3]


df.loc[[0,1]][["City","Salary"]]

print(df2[df2["Age"] > 30])

print(df2[(df2["Age"] > 30) & (df2["City"] == 'Paris')])