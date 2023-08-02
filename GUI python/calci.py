from tkinter import *
def click(event):
    global value
    text=event.widget.cget("text")
    print(text)
    if text =="=":
        if value.get().isdigit():
            values=int(value.get())
        else:
            values=eval(calci.get())
            value.set(values)
            calci.update()
    elif text=="C":
        value.set("")
        calci.update() 
    else:
        value.set(value.get()+text)
        calci.update()
calculator=Tk()
calculator.geometry("500x500")
calculator.title("CALCULATOR")
value=StringVar()
value.set("")
Heading=Label(text="Enter any two numbers \n Choose any operation",bg="teal",
              fg="black",font="comicsansms 20 bold")
Heading.pack(fill=BOTH)
calci= Entry(calculator, textvar=value,font="comicsansms 20 bold")
calci.pack(padx=15, pady=15, fill=BOTH)
numbers= [
    ("7", "8", "9", "+"),
    ("4", "5", "6", "-"),
    ("1", "2", "3", "*"),
    ("C", "0", "=", "/")]
for x in numbers:
    frame = Frame(calculator)
    frame.pack(fill=BOTH, expand=True)
    for text in x:
        numbers= Button(frame, text=text, font="comicsansms 20 bold")
        numbers.pack(side=LEFT, fill=BOTH, padx=5,pady=5,expand=TRUE)
        numbers.bind("<Button-1>",click)
calculator.mainloop()