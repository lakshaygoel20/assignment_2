#question 1
import re
li = []
def split_id(email):
    s = re.split('[@.]',email)
    li.append(s)
x=0
while x<3 :
    email = input('enter email  :  ')
    split_id(email)
    x=x+1
print('the list is :')    
print(li)
print('#'*14)
#question 2
import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
ele = re.findall(r'[bB]\w+', text)
print(ele)
print('#'*14)
#question 3
import re
sentence = "A, very very; irregular_sentence"
s = re.sub('[\W]',' ',sentence)
print(s)
print('#'*14)

