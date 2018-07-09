#question 1
import pymysql as pm
try:
    con = pm.connect( host='localhost', database = 'd', user = 'root', password = 'jojo')
    cursor = con.cursor()
    query = 'create table book( book_id int(5) primary key, title_id int(5), location varchar (10), genre varchar(10))'
    cursor.execute(query)
    print('book table made')
    cursor = con.cursor()
    query = 'create table titles(title_id int(5) primary key,title_name varchar(10),publisher_id int (10))'
    cursor.execute(query)
    print('titles table made')
    cursor = con.cursor()
    query = 'create table publisher(publisher_id int(5) primary key,name varchar(10),address varchar (10),zip_id int(10))'
    cursor.execute(query)
    print('publisher table made')
    cursor = con.cursor()
    query = 'create table zip_codes(zip_id int(5) primary key,city varchar(10),state varchar (10),zip_code int(5))'
    cursor.execute(query)
    print('zip codes table made')
    cursor = con.cursor()
    query = 'create table author_titles(author_title_id int(5) primary key,title_id varchar(10),author int (10))'
    cursor.execute(query)
    print('author title table made')
    cursor = con.cursor()
    query = 'create table author(author_id int(5) primary key,first_name varchar(10),last_name varchar (10))'
    cursor.execute(query)
    print('auther table made')
except pm.DatabaseError as e :
    if con :
        con.rollback()
        print('problem',e)
finally:
    cursor.close()
    con.close()
print('#'*14)
#question 2
try:
    con = pm.connect( host='localhost', database = 'd', user = 'root', password = 'jojo')
    cursor = con.cursor()
    query_insert = "insert into book values(1,2323,'james','comedy')"
    cursor.execute(query_insert)
    query_insert = "insert into titles values(1,'jojo',6222)"
    cursor.execute(query_insert)
    query_insert = "insert into publisher values(621,'karan','U.K',24787)"
    cursor.execute(query_insert)
    query_insert = "insert into zip_codes values(24787,'roorkee','uttrakhand',87)"
    cursor.execute(query_insert)
    query_insert = "insert into author_titles values(123,234,654)"
    cursor.execute(query_insert)
    query_insert = "insert into author values(622,'lakshay','goel')"
    cursor.execute(query_insert)
    print('queries have been  inserted in all the above  tables ')
    con.commit()
except pm.DatabaseError as e :
    if con :
        con.rollback()
        print('problem',e)
finally:
    cursor.close()
    con.close()

try:
    con = pm.connect(host='localhost', database='d', user='root',password='jojo')
    cursor = con.cursor()
    
    query_select = 'select * from book'
    cursor.execute(query_select)
    
    data = cursor.fetchall()
    for row in data:
        print("book_id: {}, title_id: {}, location : {} ,genre : {}".format(row[0],row[1],row[2],row[3]))
        print('after updation the table is : ')
    query = "update book set location = 'U.K' where location= 'james' "
    cursor.execute(query)
    query_select = 'select * from book'
    cursor.execute(query_select)
    data = cursor.fetchall()
    for row in data:
        print("book_id: {}, title_id: {}, location : {} ,genre : {}".format(row[0],row[1],row[2],row[3]))
except pm.DatabaseError as e:
    if con:
        con.rollback()
        print("problem",e)

finally:
    cursor.close()
    con.close()    
