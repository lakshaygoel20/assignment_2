#question 1
class circle:
    def __init__(self,r):
        self.radius = r
    def circum(self):
        print("the circumference %f \n"%( 2*3.14*self.radius))
    def area(self):
        print('the area  is %.2f '%(3.14*self.radius*self.radius))
x=int(input('enter radius of  circle : '))
circ_1 = circle(x)
circ_1.circum()
circ_1.area()
print('#'*14)
#question 2
class student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
    def disp(self):
        print('name is : %s'%(self.name))
        print('roll no.  is : %d'%(self.roll))
x=input('enter name : ')
y = int(input('enter roll no. '))
stu_1 = student(x,y)
stu_1.disp()
print('#'*14)
#question 3
class temp:
    def __init__(self,cel,far):
        self.celc = cel
        self.far = far
    def con_farh(self):
        farh = (self.celc * 1.8)+32
        print('the %d celcius is equal to %f farenhiet'%(self.celc,farh))
    def con_celc(self):
        celcius = (self.far - 32)* 0.555
        print('the %d far is equal to %f celcius'%(self.far,celcius))
cels = int(input('enter celcius : '))
farh = int(input('enter farhenhiet : '))
tem = temp(cels,farh)
tem.con_farh()
tem.con_celc()
print('#'*14)
#question 4
class mov_detail:
    def __init__(self,m,a,y,r):
        self.movie = m
        self.artist = a
        self.year = y
        self.rating = r
    def display(self):
        return('name of movie is : %s , artist is %s releasing in year %d with rating of %d'%(self.movie,self.artist,self.year,self.rating))
    def update(self,new):
        self.movie = new
nam = input('enter name of movie : ')
art = input('enter name of artist : ')
year = int(input('enter year of release : '))
rate = int(input('enter  a rating of movie : '))
obj=mov_detail(nam,art,year,rate)
print(obj.display())
j = input('enter new movie')
obj.update(j)
print(obj.display())
print('#'*14)
#question 5
class expenditure :
    def __init__(self,exp,sav):
        self.exp = exp
        self.sav = sav
    def disp_ex(self):
        print('the monthly expenditure is : %d'%(self.exp))
        print('the monthly saving is : %d'%(self.sav))
    def calc_sal(self):
        self.sal = self.exp + self.sav
    def disp_sal(self):
        print('the total salary is : %d'%(self.sal))
ex = int(input('enter expenditure :'))
savi = int(input('enter saving :'))
per = expenditure(ex,savi)
per.disp_ex()
per.calc_sal()
per.disp_sal()
print('#'*14)    
