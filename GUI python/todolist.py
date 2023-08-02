from tkinter import *
def enter():
    text=""
    def add():
        text=add_task.get(1.0,"end-1c")
        list.insert(END,text)
        t1.destroy()
    t1=Tk()
    t1.title("Add task")
    show=Label(t1,text="Add tasks",font="comicsansms 20 bold")
    show.pack()
    add_task=Text(t1,font="comicsansms 10")
    add_task.pack()
    done=Button(t1,text="Submit",command=add)
    done.pack()
    t1.mainloop()
def dele():
    select=list.curselection()
    list.delete(select[0])
def complete():
    mark=list.curselection()
    tem=mark[0]
    marked=list.get(mark)
    marked=marked+"(completed)"
    list.delete(tem)
    list.insert(tem,marked)
todolist=Tk()
todolist.geometry("600x500")
todolist.title("To-Do-List")
Heading=Label(text="ToDo List",bg="teal",fg="black",font="comicsansms 30 bold")
Heading.pack(fill=BOTH)
title=Label(text="Your tasks are:",font="comicsansms 20 bold")
title.pack()
frame=Frame(todolist)
frame.pack()
list=Listbox(frame,bg="white",fg="black",height=5,width=500,font="comicsansms 20 bold")
list.pack(side=LEFT,fill=BOTH)
entry=Button(todolist,text="Add task",command=enter,borderwidth=2,bg="pink",fg="black",font="comicsansms 10")
entry.pack(side=LEFT,padx=5)
delete=Button(todolist,text="Delete selected task",command=dele,borderwidth=2,bg="pink",fg="black",font="comicsansms 10")
delete.pack(side=LEFT,padx=5)
complete=Button(todolist,text="Mark as completed",command=complete,borderwidth=2,bg="pink",fg="black",font="comicsansms 10")
complete.pack(side=LEFT,padx=5)
todolist.mainloop()