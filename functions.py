# question 1
def ar_circle(rad):
    area = rad*rad*3.14
    print('area of circle with radius %.2f is %.2f '%(rad,area))
radius=float(input('enter radius of circle'))
ar_circle(radius)
print('#'*14)
#question 2
def perf(limit):
    for n in range(2,limit):
        sum = 0
        for i in range(1, n):
            if n % i != 0:
                sum += i
                if (sum == n):
                    print('%d is perfect no. between 1 and %d'%(n,limit))
            else:
                print('%d is not a perfect number'%(n))
limit=int(input('enter limit'))
perf(limit)
print('#'*14)
#question 3
def mult(num):
    if(num==0):
        print(' end')
    else:
        print('12 * %d is %d'%(num,12*num))
        mult(num-1)
numb=int(input('enter a number'))
mult(numb)
print('#'*14)
#question 4
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("%d to the power %d is : "%(base,exp),power(base,exp))
print('#'*14)
#question 5
def fact(num):
    if num==1:
        return 1
    else:
        return(num*fact(num-1))
y=int(input('enter how many factorials you want to find: '))
dicto = {}
for ele in range(0,y):
    x=int(input('enter no. to find factorial: '))
    print('the factorial of %d is '%(x),fact(x))
    dicto[x]=fact(x)
    print('the current dictonary is :',dicto)
print("#"*14)             
