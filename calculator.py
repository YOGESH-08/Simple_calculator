from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("Basic calculator")
root.geometry('570x600')
root.resizable(False,False)
root.configure(bg="black")
label=Label(root,height=3,width=570,text=" ",font=("arial",20))
label.pack()
eq=" "
label.configure(text='')
def clear():
    global eq
    eq=""
    label.configure(text=" ")
def calculations(value):
    global eq
    global val
    val=value
    eq+=value
    label.configure(text=eq)
def ans():
    global eq
    st=str(eq)
    if '/0' in st:
        messagebox.showerror("ZeroDivisionError","Error")
        eq=" "
        label.configure(text=eq)
    result=eval(eq)
    label.configure(text=result)
    eq=""
def back():
    global eq
    eq1=list(eq)
    del eq1[len(eq)-1]
    eq=''.join(eq1)
    label.configure(text=eq)



button=Button(root,text='C',height=1,width=5,bg="blue",fg="white",font=("arial",30,"bold"),command=lambda:clear())
button.place(x=10,y=106)
button=Button(root,text='/',height=1,width=5,bg="#2a2d36",fg="white",font=("arial",30,"bold"),command=lambda:calculations("/"))
button.place(x=150,y=106)
button=Button(root,text='bksc',height=1,width=5,bg="blue",fg="white",font=("arial",30,"bold"),command=lambda:back())
button.place(x=290,y=106)
button=Button(root,text='(',height=1,width=2,bg="#2a2d36",fg="white",font=("arial",30,"bold"),command=lambda:calculations("("))
button.place(x=430,y=106)
button=Button(root,text=')',height=1,width=2,bg="#2a2d36",fg="white",font=("arial",30,"bold"),command=lambda:calculations(")"))
button.place(x=500,y=106)
button=Button(root,text='7',height=1,width=5,bg="#2a2d36",fg="white",font=("arial",30,"bold"),command=lambda:calculations("7"))
button.place(x=10,y=200)
button=Button(root,text='4',height=1,width=5,bg="#2a2d36",fg="white",font=("arial",30,"bold"),command=lambda:calculations("4"))
button.place(x=10,y=300)
button=Button(root,text='1',height=1,width=5,bg="#2a2d36",fg="white",font=("arial",30,"bold"),command=lambda:calculations("1"))
button.place(x=10,y=400)
button=Button(root,text='0',height=1,width=5,bg="#2a2d36",fg="white",font=("arial",30,"bold"),command=lambda:calculations("0"))
button.place(x=10,y=500)
button=Button(root,text='.',height=1,width=5,bg="#2a2d36",fg="white",font=("arial",30,"bold"),command=lambda:calculations("."))
button.place(x=150,y=500)
button=Button(root,text='8',height=1,width=5,bg="#2a2d36",fg="white",font=("arial",30,"bold"),command=lambda:calculations("8"))
button.place(x=150,y=200)
button=Button(root,text='5',height=1,width=5,bg="#2a2d36",fg="white",font=("arial",30,"bold"),command=lambda:calculations("5"))
button.place(x=150,y=300)
button=Button(root,text='2',height=1,width=5,bg="#2a2d36",fg="white",font=("arial",30,"bold"),command=lambda:calculations("2"))
button.place(x=150,y=400)
button=Button(root,text='9',height=1,width=5,bg="#2a2d36",fg="white",font=("arial",30,"bold"),command=lambda:calculations("9"))
button.place(x=290,y=200)
button=Button(root,text='6',height=1,width=5,bg="#2a2d36",fg="white",font=("arial",30,"bold"),command=lambda:calculations("6"))
button.place(x=290,y=300)
button=Button(root,text='3',height=1,width=5,bg="#2a2d36",fg="white",font=("arial",30,"bold"),command=lambda:calculations("3"))
button.place(x=290,y=400)
button=Button(root,text='%',height=1,width=5,bg="#2a2d36",fg="white",font=("arial",30,"bold"),command=lambda:calculations("/100"))
button.place(x=290,y=500)
button=Button(root,text='x',height=1,width=5,bg="#2a2d36",fg="white",font=("arial",30,"bold"),command=lambda:calculations("*"))
button.place(x=430,y=200)
button=Button(root,text='-',height=1,width=5,bg="#2a2d36",fg="white",font=("arial",30,"bold"),command=lambda:calculations("-"))
button.place(x=430,y=300)
button=Button(root,text='+',height=1,width=5,bg="#2a2d36",fg="white",font=("arial",30,"bold"),command=lambda:calculations("+"))
button.place(x=430,y=400)
button=Button(root,text='=',height=1,width=5,bg="blue",fg="white",font=("arial",30,"bold"),command=lambda:ans())
button.place(x=430,y=500)
root.mainloop()
