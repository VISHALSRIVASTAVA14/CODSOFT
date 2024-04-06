#1)importing the module
from tkinter import*
from tkinter import messagebox

#5)create functions

def new_task():
    task=my_entry.get()
    if task!="":
        lb.insert(END,task) #(POSITION,ITEM)
        my_entry.delete(0,"end")
    else:
        messagebox.showwarning("warning","PLEASE ENTER SOME TASK")

def delete_task():
    lb.delete(ANCHOR)

#2)configure and create mainwindow
window=Tk()
window.title("TO-DO LIST")
window.geometry("500x450+500+50") #500 width, 450 height, 500 position from x-axis, 200 position from y-axis
window.config(bg="#223441")
window.resizable(width=False,height=False)

#icon
icon=PhotoImage(file="icon.png")
window.iconphoto(False,icon)

#4)create widgets(frame,listbox,scrollbar,entry,button)
frame=Frame(window)
frame.pack(pady=10)

lb=Listbox(frame,width=25,height=8,font=("arial",18,"bold"),bd=1,activestyle="none")
lb.pack(side=LEFT,fill=BOTH)

task_list=["EAT APPLE","DRINK WATER","GO TO GYM","BADMINTON"]
for i in task_list:
    lb.insert(END,i)
    
sb=Scrollbar(frame)
sb.pack(side=RIGHT,fill=BOTH)
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry=Entry(window,font=("arial",24))
my_entry.pack(pady=20)

button_frame=Frame(window)
button_frame.pack(pady=20)

add_task_button=Button(button_frame,text="ADD TASK",font=("arial",14,"bold"),bg="red",command=new_task)
add_task_button.pack(side=LEFT,fill=BOTH)

delete_task_button=Button(button_frame,text="DELETE TASK",font=("arial",14,"bold"),bg="yellow",command=delete_task)
delete_task_button.pack(side=RIGHT,fill=BOTH)

#3)create mainloop
window.mainloop()


