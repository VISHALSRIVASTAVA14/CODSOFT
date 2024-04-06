import tkinter
from tkinter import *
import random

def user_score():
    score=int(label5.cget("text"))
    score+=1
    label5.configure(text=str(score))

def comp_score():
    score=int(label7.cget("text"))
    score+=1
    label7.configure(text=str(score))

def show(value):
    eqn=""
    eqn+=value
    a=["ROCK","PAPER","SCISSOR"]
    computer=random.choice(a)
    if(eqn=="ROCK"):
        if(computer=="ROCK"):
            label3.config(text="COMPUTER'S CHOICE: ROCK....HENCE ITS A TIE")
        elif(computer=="SCISSOR"):
            label3.config(text="COMPUTER'S CHOICE: SCISSOR....HENCE ITS A WIN")
            user_score()
        else:
            label3.config(text="COMPUTER'S CHOICE: PAPER.....HENCE ITS A LOSE")
            comp_score()
    elif(eqn=="PAPER"):
        if(computer=="ROCK"):
            label3.config(text="COMPUTER'S CHOICE: ROCK....HENCE ITS A WIN")
            user_score()
        elif(computer=="SCISSOR"):
            label3.config(text="COMPUTER'S CHOICE: SCISSOR....HENCE ITS A LOSE")
            comp_score()
        else:
            label3.config(text="COMPUTER'S CHOICE: PAPER.....HENCE ITS A TIE")
    else:
        if(computer=="ROCK"):
            label3.config(text="COMPUTER'S CHOICE: ROCK....HENCE ITS A LOSE")
            comp_score()
        elif(computer=="SCISSOR"):
            label3.config(text="COMPUTER'S CHOICE: SCISSOR....HENCE ITS A TIE")
        else:
            label3.config(text="COMPUTER'S CHOICE: PAPER.....HENCE ITS A WIN")
            user_score()

def play():
    label3.config(text="")

window=Tk()
window.title("ROCK-PAPER-SCISSORS")
window.geometry("570x660+500+20")
window.config(bg="#00008B")
window.resizable(False,False)

label1=Label(window,text="ROCK-PAPERS-SCISSORS",font=("lucida sans",15,"bold"),bg="yellow",fg="white",height=1,width=20,bd=2)
label1.pack(pady=2)

label2=Label(window,
             text="INSTRUCTIONS:\n\n1)CHOOSE AN OPTION\n2)ROCK>SCISSORS & ROCK<PAPER\n3)PAPER>ROCK & PAPER<SCISSORS\n4)SCISSOR>PAPER & SCISSOR<ROCK",
             font=("canva sans",15,"bold","underline"),anchor="w",justify="left",bg="red",fg="white",height=8,bd=2)
label2.pack(pady=2,fill=BOTH)

label3=Label(window,
             font=("lucida handwriting",10,"bold"),
             width=40,height=3,bg="white",fg="black",bd=2)
label3.pack(pady=3)

rock_button = Button(window,text="ROCK",font=("lucida handwriting",20,"bold"),bg="black",fg="white",height=2,width=8,command=lambda: show("ROCK"))
rock_button.place(x=20,y=360)

paper_button = Button(window,text="PAPER",font=("lucida handwriting",20,"bold"),bg="black",fg="white",height=2,width=8,command=lambda: show("PAPER"))
paper_button.place(x=200,y=360)

scissor_button = Button(window,text="SCISSOR",font=("lucida handwriting",20,"bold"),bg="black",fg="white",height=2,width=8,command=lambda: show("SCISSOR"))
scissor_button.place(x=390,y=360)

play_again_button = Button(window,text="PLAY AGAIN",font=("lucida handwriting",20,"bold"),bg="black",fg="white",height=2,width=15,command=lambda: play())
play_again_button.place(x=150,y=480)

label4=Label(window,text="YOUR SCORE",font=("lucida handwriting",10,"bold"),height=1,width=20,bg="white",fg="black")
label4.place(x=20,y=600)

label5=Label(window,text="0",font=("lucida handwriting",10,"bold"),height=1,width=10,bg="white",fg="black")
label5.place(x=250,y=600)

label6=Label(window,text="COMPUTER SCORE",font=("lucida handwriting",10,"bold"),height=1,width=20,bg="white",fg="black")
label6.place(x=20,y=630)

label7=Label(window,text="0",font=("lucida handwriting",10,"bold"),height=1,width=10,bg="white",fg="black")
label7.place(x=250,y=630)

window.mainloop()
