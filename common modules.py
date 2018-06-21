#question 1
time_tuple = '''TIME TUPLE :  We represent time in a way that’s easy for us to understand.
However, Python stores it in tuples.These python tuples are made of nine numbers.
Leap seconds are added to make up to Earth’s slowing rotation. When DST is 0,it isn’t
applied. When it’s 1, it is applied. However, when it is -1, it is up to the library
to determine that.This tuple has an equivalent struct_time structure.'''
print(time_tuple)
print('#'*13)
#question 2
import datetime
current = datetime.datetime.now()
print('formatted date and time is : ',current.strftime("%d/%B/%Y"))
print('#'*13)
#question 3
current = datetime.datetime.now()
print('the date and time is : ',current.strftime("%d/%m/%Y"))
x=current.month
print("the  extracted month is : ",x)
print('#'*13)
#question 4
current = datetime.datetime.now()
print(' the date and time is : ',current.strftime("%d/%m/%Y"))
x=current.day
print("the  extracted day is : ",x)
print('#'*13)
#question 5
a = '2018-06-21'
datee = datetime.datetime.strptime(a, "%Y-%m-%d")
print('the date is : ',datee)
y=datee.day
print('the extracted date from this time is :',y)
print('#'*13)
#question 6
import time
x=time.asctime(time.localtime())
print('local time is : ',x)
print('#'*13)
#question 7
import math
x= int(input('enter a number to find uts factorial : '))
print('the factorial is : ',math.factorial(x))
print('#'*13)
#question 8 is optional
#question 9
import os
print('the current directory is : ',os.getcwd())
print('#'*13)
