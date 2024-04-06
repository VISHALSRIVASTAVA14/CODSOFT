import tkinter
from tkinter import *

window=Tk()
window.title("CALCULATOR")
window.geometry("500x420+500+50")
window.resizable(width=False,height=False)
window.config(bg="black")

screen=Label(window,font=("arial",18,"bold"),width=25,height=2)
screen.pack(fill=BOTH)

eqn=""

def clear():
    global eqn
    eqn=""
    screen.config(text=eqn)

def show(value):
    global eqn
    eqn=eqn+value
    screen.config(text=eqn)

def calculate():
    global eqn
    result=""
    if eqn!="":
        result=eval(eqn)
    else:
        result="ERROR"
        eqn=""
    screen.config(text=result)
        

Button(window,text="C",font=("arial",18,"bold"),bg="blue",fg="white",height=1,width=5,bd=1,command=lambda: clear()).place(x=10,y=80)
Button(window,text="/",font=("arial",18,"bold"),bg="grey",fg="white",height=1,width=5,bd=1,command=lambda: show("/")).place(x=140,y=80)
Button(window,text="%",font=("arial",18,"bold"),bg="grey",fg="white",height=1,width=5,bd=1,command=lambda: show("%")).place(x=270,y=80)
Button(window,text="*",font=("arial",18,"bold"),bg="grey",fg="white",height=1,width=5,bd=1,command=lambda: show("*")).place(x=400,y=80)

Button(window,text="7",font=("arial",18,"bold"),bg="grey",fg="white",height=1,width=5,bd=1,command=lambda: show("7")).place(x=10,y=150)
Button(window,text="8",font=("arial",18,"bold"),bg="grey",fg="white",height=1,width=5,bd=1,command=lambda: show("8")).place(x=140,y=150)
Button(window,text="9",font=("arial",18,"bold"),bg="grey",fg="white",height=1,width=5,bd=1,command=lambda: show("9")).place(x=270,y=150)
Button(window,text="-",font=("arial",18,"bold"),bg="grey",fg="white",height=1,width=5,bd=1,command=lambda: show("-")).place(x=400,y=150)

Button(window,text="4",font=("arial",18,"bold"),bg="grey",fg="white",height=1,width=5,bd=1,command=lambda: show("4")).place(x=10,y=220)
Button(window,text="5",font=("arial",18,"bold"),bg="grey",fg="white",height=1,width=5,bd=1,command=lambda: show("5")).place(x=140,y=220)
Button(window,text="6",font=("arial",18,"bold"),bg="grey",fg="white",height=1,width=5,bd=1,command=lambda: show("6")).place(x=270,y=220)
Button(window,text="+",font=("arial",18,"bold"),bg="grey",fg="white",height=1,width=5,bd=1,command=lambda: show("+")).place(x=400,y=220)

Button(window,text="1",font=("arial",18,"bold"),bg="grey",fg="white",height=1,width=5,bd=1,command=lambda: show("1")).place(x=10,y=290)
Button(window,text="2",font=("arial",18,"bold"),bg="grey",fg="white",height=1,width=5,bd=1,command=lambda: show("2")).place(x=140,y=290)
Button(window,text="3",font=("arial",18,"bold"),bg="grey",fg="white",height=1,width=5,bd=1,command=lambda: show("3")).place(x=270,y=290)
Button(window,text="=",font=("arial",18,"bold"),bg="orange",fg="white",height=3,width=5,bd=1,command=lambda: calculate()).place(x=400,y=290)

Button(window,text="0",font=("arial",18,"bold"),bg="grey",fg="white",height=1,width=14,bd=1,command=lambda: show("0")).place(x=10,y=350)
Button(window,text=".",font=("arial",18,"bold"),bg="grey",fg="white",height=1,width=5,bd=1,command=lambda: show(".")).place(x=270,y=350)


window.mainloop()
