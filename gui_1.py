# question 1
from tkinter import *
root = Tk()
root.geometry('500x500')
lbL = Label(root,text='hello world')
lbL.pack()
button = Button (root, text = "Exit", command = root.quit)
button.pack(side=BOTTOM)
root.mainloop()
print('#'*15)
# question 2
from tkinter import *
root = Tk()
root.geometry('500x500')
labL_2 = Label(root,text='this is new text')
labL_2.pack()
def show_text() :
    lbL = Label(root,text='hello world')
    lbL.pack()
button = Button (root, text = "click here", command = show_text)
button.pack()
button_1 = Button (root, text = "Exit", command = root.destroy)
button_1.pack(side=BOTTOM)
root.mainloop()
print('#'*15)
# question 3
from tkinter import *
root = Tk()
root.geometry('500x500')
lbL_2 = Label(root,text='this is our Label, click button to change it',background='blue')
def change_label() :
    lbL_2.config(text="label is changed",background='yellow')
button = Button (root, text = "click here", command = change_label)
button.pack()
lbL_2.pack()
button_1 = Button (root, text = "Exit", command = root.destroy)
button_1.pack(side=BOTTOM)
root.mainloop()
print('#'*15)
# question 4
root = Tk()
root.geometry('500x500')
lbL_2 = Label(text='enter any text',background='blue')
lbL_2.pack()
entry_1 = Entry(lbL_2)
entry_1.pack()
def show_text() :
    ent = entry_1.get()
    labL  = Label(root,text ='your text is :  \n %s'%(ent),background='yellow')
    labL.pack()
button = Button (root, text = "show your text", command = show_text)
button.pack()
button_1 = Button (root, text = "Exit", command = root.destroy)
button_1.pack(side=BOTTOM)
root.mainloop()
print('#'*15)


