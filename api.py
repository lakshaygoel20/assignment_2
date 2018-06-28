# question 1
print('''The fundamental difference,is that XML is a markup language (as it actually says in its name), whereas JSON is a way of representing objects (as also noted in its name).

A markup language is a way of adding extra information to free-flowing plain text''')
print('#'*14)
# question 2
import socket
x= int(input('enter how many  ip addresses you want to find.'))
for i in range(0,x):
    addr1 = input('enter website to find its ip address')
    ip_1 = socket.gethostbyname(addr1)
    print('the ip address of %s is :'%(addr1),ip_1)
print('#'*14)
# question 3
print('''The GET method requests a representation of the specified resource. Requests using GET should only retrieve data and should have no other effect. (This is also true of some other HTTP methods.)[1] The W3C has published guidance principles on this distinction, saying, "Web application design should be informed by the above principles, but also by the relevant limitations''')
print('''The POST method requests that the server accept the entity enclosed in the request as a new subordinate of the web resource identified by the URI. The data POSTed might be, for example, an annotation for existing resources; a message for a bulletin board, newsgroup, mailing list, or comment thread; a block of data that is the result of submitting a web form to a data-handling process; or an item to add to a database''')
print('''The PUT method requests that the enclosed entity be stored under the supplied URI. If the URI refers to an already existing resource, it is modified; if the URI does not point to an existing resource, then the server can create the resource with that URI''')
print('''The DELETE method deletes the specified resource.''')
print('#'*14)
# question 4
print('''An API (Application Programming Interface) is a collection of interface routines to a particular library, collection of libraries or operating system. This allows application programmers to use the functions in the libraries without needing to know the internal structure of the system they are accessing.

A DLL (Dynamic Link Library) is an object module comprising a set of related routines that may be part of a larger API. DLLs are loaded into memory on demand where their code may be shared by many application programs.''')
print('#'*14)
# question 5 skip said by sir
