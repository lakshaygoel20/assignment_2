#question 1
a=3
try :
    a=a/(a-3)
    print(a)
except ZeroDivisionError as err :
    print('an error has occured')
    print(err)
print('#'*14)
#question 2
l=[1,2,3]
try :
    print(l[3])
except Exception as err :
    print('an error has occured :')
    print(err)
print('#'*14)
#question 3
print('an exception\n NameError')
print('#'*14)
#question 4
print(' the output of the question is : \n-5 \n a/b result in zero')
print('#'*14)
#question 5
try:
    from jojo import *
except Exception as e :
    print('the import error  :')
    print(e)    
li = ['a','b','c','d']
try :
    li[5]
except Exception as e :
    print('the index error  :')
    print(e)
abc = 'dog'
try :
    int(abc)
    
except Exception as e :
    print('the value error :')
    print(e)
print('#'*14)
#question 6
class under_age(Exception):
    def __init__(self,age):
        self.age = age
        print('you are %d years old, please enter age above 18 to proceed'%(self.age))
def ent_age():
    try :
        x = int(input('enter your age :'))
        if x<18 :
            raise under_age(x)
        print('now you can book tickets for race 3 !!!! as you are above 18')
    except under_age as err :
        print('this is an under age error :')
        ent_age()
ent_age()        
print('#'*14)
