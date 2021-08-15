from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import sys,time,os
class Main():
    def __init__(self,root):
        def message(self):
            messagebox.showinfo("پیام","شماره من در واتساپ 09913767552")
            pass
        label=Label(root,text="ما را در شبکه های مجازی دنبال کنید",font="arial 20",
        bg="green",fg="red")
        label.pack(fill=BOTH)
        label_1=Label(root,text="واتساپ",bg="white",fg="red",font="arial 25",
        padx=10,pady=10,bd=15)
        label_1.bind("<ButtonPress-1>",message)
        label_1.bind("<ButtonPress-2>",message)
        label_1.bind("<ButtonPress-3>",message)
        label_1.place(x=180,y=200)
        pass
if __name__=="__main__":
    root=Tk()
    root.geometry("500x500")
    root.title("Program")
    root.configure(background="black")
    Main(root)

    root.mainloop()
