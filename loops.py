#question 1
list_1=[]
for i in range(0,10):
    y=int(input("enter  integer : "))
    list_1.append(y)
print('the no.s are :')    
for i in range(0,10):
    print(list_1[i])
print('#'*15)
#question 2
x=1
while(x<2):
    print('we are in loop')
    x=x-1
print('#'*15)
#question 3
list_1 = []
for i in range(0,5):
	number = int(input('Please enter a number: ')) 
	list_1.append(number)
print('list is :',list_1)
list_2 = []
for i in list_1:
    num = i*i
    list_2.append(num)
print('the new list is : ',list_2)    
print('#'*15)
#question 4
list_1=[2,3,'abc',23.4,'def','22.8']
num_list=[]
flo_list=[]
strn_list=[]
print('the  list is :',list_1)
for i in list_1:
    if(type(i)==int):
        num_list.append(i)
    elif(type(i)==float):
        flo_list.append(i)
    elif(type(i)==str):
        strn_list.append(i)    
print('the integer list is :',num_list)  
print('the float list is :',flo_list)
print('the string list is :',strn_list)  
print('#'*15)
#question 5
list_1=[]
list_2=[]
for i in range(1,101):
    if(i%2==0):
        list_1.append(i)
    else:
        list_2.append(i)    
print('the even list is :',list_1)  
print('the odd list is :',list_2)
print('#'*15)
#question 6
for i in range(0,5):
    print('*'*i)
print('#'*15)
#question 7

dicct={'a':1,'b':2,'c':3,'d':4}
for i in range(len(dicct)):
    print("the elements are ",dicct[i])
