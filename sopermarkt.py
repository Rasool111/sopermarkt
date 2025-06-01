from tkinter import *
from tkinter import messagebox
import webbrowser
import os
import sys

screen = Tk()
def exit_1():
    sys.exit()
def quit():
    messagebox.showinfo("Exit", "Thanks for using our application...")
    sys.exit()
def login():
    username = Entery1.get()
    password = Entery2.get()
    if username == "admin" and password == "admin":
        messagebox.showinfo("Login ", """Welcome to our application...
        Your account has been created successfully!""")

        from pysoper import run
        run()


    elif username == "admin":
        messagebox.showerror("Login ", "Invalid password")
    elif password == "admin":
        messagebox.showerror("Login ", "Invalid username")
    else:
        messagebox.showerror("Login ", "Invalid username or password")
screen.geometry("800x450+280+50")
screen.resizable(False,False)
screen.title("MOATH_Supermarket")
screen.iconbitmap(r"3695283.ico")
photo=PhotoImage(file="pngtree-supermarket-clipart-cartoon-grocery-store-with-fruits-and-vegetables-vector-png-image_6825233.png")
img=Label(screen,image=photo,bg="#0B2F3A")
title = Label(screen, text="MOATH_Supermarket System ", font=("Arial", 20 ,'bold'), fg="green" , bg="white")
title.pack(fill=X)
F1=Frame(screen,width=230,height=420,bg="#0B2F3A")
F1.place(x=570,y=37)
F2=Frame(screen,width=570,height=120,bg="#0B2F3A")
F2.place(x=0,y=330)
photo1=PhotoImage(file="resized_110x110_transparent.png")
img2=Label(F2,image=photo1,bg="white")
L1=Label(F2,text="UserName" ,fg='gold',bg='#0B2F3A',font=("Arial", 12 ,'bold'))
L2=Label(F2,text="Password" ,fg='gold',bg='#0B2F3A',font=("Arial", 12 ,'bold'))
L1.place(x=150,y=12)
L2.place(x=150,y=50)
Entery1=Entry(F2,width=40,font=("Arial", 12 ,'bold'),justify="center")
Entery2=Entry(F2,width=40,font=("Arial", 12 ,'bold'),show="*",justify="center")
Entery1.place(x=250,y=12)
Entery2.place(x=250,y=50)
Titel1=Label(F1 ,text="""SuperMarket System
نظام سوبر ماركت""",font=("Arial", 16 ,'bold'),fg="white" , bg="#0B2F3A")
Titel2=Label(F1,text="Developed by Muath © 2025",font=("Arial", 12 ,'bold'),fg="white" , bg="#0B2F3A")
Titel3=Label(F1 , text="""For support or questions
 contact us via: """ ,font=("Arial", 12 ,'bold'),fg="white" , bg="#0B2F3A")
B1= Button(F1,text="Facebook",width=20 , fg="white" ,font=("Arial", 12 ,'bold'),bg="#1877F2",command=lambda:webbrowser.open("https://www.facebook.com/muath.moath/"))
B2= Button(F1,text="Instagram",width=20 , fg="white" ,font=("Arial", 12 ,'bold'),bg="#C13584",command=lambda:webbrowser.open("https://www.instagram.com/alhaq_ali1?igsh=eGYwN2p1Y3M1enZ2"))
B3= Button(F1,text="WhatsApp",width=20 , fg="white" ,font=("Arial", 12 ,'bold'),bg="#25D366",command=lambda:webbrowser.open("wa.me/qr/3SEG5JIDNYWRH1"))
B4= Button(F1,text="Telegram",width=20 , fg="white" ,font=("Arial", 12 ,'bold'),bg="#0088CC",command=lambda:webbrowser.open("https://t.me/Joad112"))
B5= Button(F1,text="Email",width=20 , fg="white" ,font=("Arial", 12 ,'bold'),bg="#CCCCCC",command=lambda:webbrowser.open("mailto:baqara2000ali@gmail.com"))
B6= Button(F1,text="Exit",width=20 , fg="white" ,font=("Arial", 12 ,'bold'),bg="RED",command=quit)
B=Button(F2,text="Login",width=40,fg="white" ,font=("Arial", 12 ,'bold'),bg="green",command=login)
B.place(x=250,y=80)
img.place(x=0,y=43,width=570,height=350)
img2.place(x=12,y=0,width=110,height=110)
Titel1.place(x=12,y=10)
Titel2.place(x=8,y=370)
Titel3.place(x=12,y=80)
B1.place(x=12,y=130)
B2.place(x=12,y=170)
B3.place(x=12,y=210)
B4.place(x=12,y=250)
B5.place(x=12,y=290)
B6.place(x=12,y=330)
screen.mainloop()
