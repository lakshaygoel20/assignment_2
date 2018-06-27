#question 1
import threading
import datetime
import time
def thread(name):
    for i in range(2):
        print(name,datetime.datetime.now())
        time.sleep(5)
        print('this statement is printed after 5 second delay:\n ',datetime.datetime.now())
threading.Thread(target=thread,args=("thread",)).start()        
print('#'*14)
#question 2
import threading
import time
def thread(name):
    for i in range(1,11):
        print('after 1 second delay')
        time.sleep(1)
        print(i)
threading.Thread(target=thread,args=("thread",)).start()
print('#'*14)
#question 3
import time
import threading
li = ['abc','def','ghi','jkl','mno']
def show_li(y):
    for i in li :
        y=2+y
        time.sleep(y)
        print('now %d sec delay :'%(y))
        print('%d list element is : '%li.index(i),i)
x = 0
threading.Thread(target = show_li, args = (x,)).start()
  print('#'*14)
#question 4
  import time
import math
import threading
x= int(input('enter no. to find factorial using thread : '))
threading.Thread(target = math.factorial , args = (x,)).start()
fact = math.factorial(x)
time.sleep(4)
print('after 4 second delay :')
print('the fact is :',fact)

print('#'*14)
