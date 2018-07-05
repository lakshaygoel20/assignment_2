#question 1
import numpy as np
a = np.random.random((10,1))
print('the array is :',a)
print('shape :',np.shape(a))
b = np.mean(a)
print('the mean of array is : ',b)
print('#'*15)
#question 2
a = np.random.random((20,1))
print('the array is :',a)
print('shape is :',np.shape(a))
b = np.var(a)
print('the variance of array is : ',b)
c = np.std(a)
print('the standard deviation  of array is : ',c)
print('#'*15)
#question 3
a = np.random.random((10,20))
print('the A array is :',a)
print('shape is :',np.shape(a))
b = np.random.random((20,25))
print('the  B array is :',b)
print('shape is :',np.shape(b))
c = np.dot(a,b)
print('the product of matrix is : ',c)
print(np.shape(c))
print('#'*15)
#question 4
A=([[1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8],
    [9],
    [10]])
import math
import numpy as np
np_arr = np.array(A)
l1=[]
def x(ele):
    y=1 / (1 + exp(-ele))
    l1.append(y)
for ele in A:
    x(ele)
B = np.array(l1)
print(B)
print('#'*15)

