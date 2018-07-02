#question 1
with open('sample.txt') as myfile:
    count = sum(1 for line in myfile)
print(count)
x = int(input('enter how many last lines you want to read(less than %d)'%(count)))
print('the last %d lines of file are :'%(x))
with open('sample.txt','r') as read_l :
    y = read_l.readlines(x)
    print(y)
print('#'*14)
#question 2
f = open('sample.txt','r')
x = f.readline()
li = {}
for word in f.read().split():
    if word not in li:
        li[word] = 1
    else:
        li[word] += 1

for k,v in li.items():
    print (k, v)
f.close    
print('#'*14)
#question 3
with open("sample.txt") as f:
    with open("out.txt", "w") as f1:
        for line in f:
            f1.write(line)
print('text copied from sample.txt to out.txt')
print('#'*14)
#question 4
with open("sample.txt") as f , open('try.txt') as g:
    for line_1,line_2 in zip(f,g):
        print(line_1+line_2)
print('#'*14)
#question 5
import random
f = open('sample.txt','w')
for i in range(10):
    data = str(random.randint(1,10))
    f.write(data)
    f.write('\n')
f.close()
f1 = open('sample.txt','r')
f2 = open('try.txt','w')
list1 = f1.readlines()
list1.sort()
f2.writelines(list1)
print(list1)
f1.close()
f2.close()
print('#'*14)
