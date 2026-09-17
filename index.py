import pandas as pd
import numpy as np


# Learning the series 
''' labels=['a','b','d','c']

arr=np.array([12,23,34,45])

d={1:10,2:20,3:30}
print(pd.Series(arr,index=labels))

print(pd.Series(d)) '''

# Learning the dataframe . multiple series 


data = [
     ['John', 'Anna', 'Peter', 'Linda'],
     [28, 34, 29, 42],
     ['New York', 'Paris', 'Berlin', 'London'],
     [65000, 70000, 62000, 85000]
]

data1={
    "name":["sanghakara"],
    "age":[22]
}

df=pd.DataFrame(data1)

colums= ["Name","Age","City","Salary"]

df1=pd.DataFrame(data,columns=colums)



print(df1['Age'])