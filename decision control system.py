#question 1
x=int(input('enter a year to find if it is leap year or not :'))
if(x%4==0):
    if(x==0):
        print('invalid year')
    else:
        print('%d is leap year..'%(x))
else:
    print('%d is not leap year.'%(x))
print('#'*15)
#question 2
length=float(input('enter length : '))
breadth=float(input('enter breadth : '))
if(length==0 or breadth==0):
    print('invalid dimension')
if(length==breadth):
    print('it is a square')
else:
    print('it is rectangle')
print('#'*15)
#question 3
age_1=int(input('enter the age of first person : '))
age_2=int(input('enter the age of second person : '))
age_3=int(input('enter the age of third person : '))
if(age_1==0 or age_2==0 or age_3==0):
    print('age cannot be zero')
if(age_1>age_2 and age_1>age_3):
    print('first person is oldest')
elif(age_2>age_1 and age_2>age_3):
    print('second person is oldest')
elif(age_3>age_1 and age_3>age_2):
    print('third person is oldest')
if(age_1<age_2 and age_1<age_3):
    print('first person is youngest')
elif(age_2<age_1 and age_2<age_3):
    print('second person is youngest')
elif(age_3<age_2 and age_3<age_1):
    print('third person is youngest')
print('#'*15)
#question 4
point=float(input('enter your points(between 1-200) : '))
if(point=<0 or point>200):
    print('invalid points')
if(point<=50 and point>0  ):
    print('sorry no prize this time...')
elif(point<=150 and point>0 ):
    print('congratulations!! you won a wooden dog')
elif(point<=180 and point>=200 and point>0 ):
    print('congratulations!! you won a book')
else:
    print('congratulations!! you won chocolates')
print('#'*15)
#question 5
cost=100
print('special 10% discount if total purchase is more than Rs.1000')
print('one unit cost Rs.100')
unit=int(input('enter no. of units to purchase'))
bill=float(cost*unit)
if(unit<=0):
    print(' please enter valid data..')
if(bill>1000):
    print('your total bill before 10% discount is :Rs.',bill)
    bill=bill-(bill*0.1)
    print('your total bill after 10% discount is :Rs.',bill)
else:
    print('your total bill is :Rs.',bill)
print('#'*15)    
