#question 1
import pandas as pd
data_1 = {
'name':pd.Series(['lakshay']),
'age':pd.Series([19]),
'mail_id':pd.Series(['lakshaygoel20@gmail.com']),
'phone':pd.Series([9870739646])
}
df = pd.DataFrame(data_1)
print(df)
data_3 = {
'name':pd.Series(['jojo']),
'age':pd.Series([20]),
'mail_id':pd.Series(['jojo@gmail.com']),
'phone':pd.Series([4326775356])
}
df_2 = pd.DataFrame(data_3)
df3 =df.append(df_2)
print('new row is added : ')
print(df3)
print('#'*15)
#question 2
import csv
import pandas as pd
a = pd.read_csv('weather.csv')
print(a)
print(80*"_")

#1
print("First 5 Rows\n")
print(a.head(5))
print(80*"_")

#2
print("First 10 Rows\n")
print(a.head(10))
print(80*"_")

#3
df = pd.DataFrame(a)
print (df. describe(include='all'))
print(80*"_")

#4
print("Last 5 Rows\n")
print(a.tail(5))
print(80*"_")

#5
z=df.loc[0]
print("First column extracted:\n")
print(z)
print(80*"*")
df = pd.DataFrame(z)
print (df. describe(include='all'))
print('#'*15)
