

#question 1
class animal:
    def __init__(self):
        print('the attributes of animals are')
    def animal_attr(self):
        print('eats')
        print('sleep')
        print('breath')
        print('runs')
class tiger(animal):
    def __init__(self):
        print('the attributes of tiger are : ')
t1 = tiger()
t1.animal_attr()
print('#'*14)
#question 2
''' the output is :
    A B
    A B
         '''
print('#'*14)
#question 3
class Cop():
    def __init__(self,name,age,work,experience,designation):
        self.name=name
        self.age=age
        self.work=work
        self.experience=experience
        self.designation=designation
    def display(self):
        print(self.name)
        print(self.age)
        print(self.work)
        print(self.experience)
        print(self.designation)
    def add(self):
        print("Add the following details",self.name)
    def update(self,n,a,w,e,d):
        self.name=n
        self.age=a
        self.work=w
        self.experience=e
        self.designation=d
        print("The Updated details are:")
        print(self.name)
        print(self.age)
        print(self.work)
        print(self.experience)
        print(self.designation)
    def updated_details(self):
        return (self.name,self.age,self.work,self.experience,self.designation)
x=Cop('jojo',22,'covert operation','2yrs','captain')
x.display()
x.update('loki',23,'info gather','5yrs','spy')
x.updated_details()
class Mission(Cop):
   def add_mission(self):
        print("The mission is alloted to:",self.updated_details())
l1=Mission('jaki',23,'Manager','5yrs','cop')
l1.add_mission()
print('#'*14)
#question 4
class Shape():
    def __init__(self,len,bre):
        self.len=len
        self.bre=bre
    def area(self,len,bre):
       print("Area is:",self.len*self.bre)
class Rectangle(Shape):
    print("Area of Reactangle")
x=Rectangle(3,4)
x.area(3,4)
class Square(Shape):
    print("Area of Square")
y=Square(5,6)
y.area(5,6)
print('#'*14)
