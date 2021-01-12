from tkinter import *
import backend

a = "Error, value(s) missing"

def view_command():
    lb1.delete(0,END)
    for row in backend.view():
        lb1.insert(END,row)

def flush_values():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END) 

def insert_command():
    lb1.delete(0,END)
    Tt=tt.get()
    At=at.get()
    Yt=yt.get()
    It=it.get()
    if Tt == "" or At == "" or Yt == "" or It == "":
        lb1.insert(END,a)
    else:
        backend.insert(Tt,At,Yt,It)  
        lb1.insert(END,[Tt,At,Yt,It]) 
    flush_values() 

def search_command():
    lb1.delete(0,END)
    Tt=tt.get()
    At=at.get()
    Yt=yt.get()
    It=it.get()
    for rows in backend.search(Tt,At,Yt,It):
        lb1.insert(END,rows)
    flush_values()   

def get_selected_row(event):
    try:
        global selected_tuple
        index = lb1.curselection()[0]
        selected_tuple = lb1.get(index)
        display_value()
    except IndexError:
        pass

def display_value():
    flush_values()
    e1.insert(END,selected_tuple[1])
    e2.insert(END,selected_tuple[2])
    e3.insert(END,selected_tuple[3])
    e4.insert(END,selected_tuple[4])

def delete_command():
    backend.delete(selected_tuple[0])
    flush_values()
    view_command()

def update_command():
    backend.update(selected_tuple[0],tt.get(),at.get(),yt.get(),it.get())
    flush_values()
    view_command()

window = Tk()

window.wm_title("Bookstore")

l1 = Label(window,text="Title")
l1.grid(row=0,column=0)

l2 = Label(window,text="Author")
l2.grid(row=0,column=2)

l3 = Label(window,text="Year")
l3.grid(row=1,column=0)

l4 = Label(window,text="ISBN")
l4.grid(row=1,column=2)

tt=StringVar() #title text
e1 = Entry(window,textvariable=tt)
e1.grid(row=0,column=1)

at=StringVar() #author text
e2 = Entry(window,textvariable=at)
e2.grid(row=0,column=3)

yt=StringVar() #year text
e3 = Entry(window,textvariable=yt)
e3.grid(row=1,column=1)

it=StringVar() #ISBN text
e4 = Entry(window,textvariable=it)
e4.grid(row=1,column=3)

lb1 = Listbox(window,height=6,width=35)
lb1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

sb2 = Scrollbar(window,orient = HORIZONTAL)
sb2.grid(row=8,column=0,columnspan=2)

lb1.configure(yscrollcommand = sb1.set)
sb1.configure(command = lb1.yview)

lb1.configure(xscrollcommand = sb2.set)
sb2.configure(command = lb1.xview)

lb1.bind('<<ListboxSelect>>',get_selected_row)

b1 = Button(window,text="View All",width=12,command = view_command)
b1.grid(row=2,column=3)

b2 = Button(window,text="Search Entry",width=12,command = search_command)
b2.grid(row=3,column=3)

b3 = Button(window,text="Add Entry",width=12,command = insert_command)
b3.grid(row=4,column=3)

b4 = Button(window,text="Update Selected",width=12,command = update_command)
b4.grid(row=5,column=3)

b5 = Button(window,text="Delete Selected",width=12,command = delete_command)
b5.grid(row=6,column=3)

b6 = Button(window,text="Close",width=12,command = window.destroy)
b6.grid(row=7,column=3)

window.mainloop()