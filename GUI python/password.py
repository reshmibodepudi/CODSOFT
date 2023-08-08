from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
def generate():
    username=usernamep.get()
    length=int(lengthp.get())
    characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(characters) for _ in range(length))
    done.config(text=f"Generated password is:{password}",font="comicsansms 10")
def accept():
    length=int(lengthp.get())
    characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(characters) for _ in range(length))
    pyperclip.copy(password)
    spam = pyperclip.paste()
    messagebox.showinfo("copied","password copied to clipboard!")
def reset():
    lengthp.delete(0,END)
    usernamep.delete(0,END)
    done.config(text="Generated password:")
passwordgenerator=Tk()
passwordgenerator.geometry("500x500")
passwordgenerator.title("Password Generator")
title=Label(text="Password Generator",fg="navyblue",font="comicsansms 15 bold")
title.grid(row=0,column=0,pady=5)
name=Label(passwordgenerator, text="Enter username:",font="comicsansms 10")
name.grid(row=1,column=0,pady=3)
len=Label(passwordgenerator, text="Enter password legth:",font="comicsansms 10")
len.grid(row=2,column=0,pady=3)
done= Label(passwordgenerator, text="Generated password:",font="comicsansms 10")
done.grid(row=3,column=0,pady=3)
usernamep = Entry(passwordgenerator,font="comicsansms 10")
usernamep.grid(row=1,column=1,pady=3)
lengthp = Entry(passwordgenerator,font="comicsansms 10")
lengthp.grid(row=2,column=1,pady=3)
gen= Button(passwordgenerator, text="GENERATE PASSWORD", command=generate,borderwidth=2,
                         bg="navyblue",fg="white",font="comicsansms 10")
gen.place(x=200,y=130)
accept=Button(passwordgenerator, text="ACCEPT", command=accept,fg="black",font="comicsansms 10")
accept.place(x=240,y=170)
reset=Button(passwordgenerator, text="RESET", command=reset,fg="navyblue",font="comicsansms 10")
reset.place(x=245,y=200)
passwordgenerator.mainloop()
