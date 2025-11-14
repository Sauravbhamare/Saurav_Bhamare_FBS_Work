from tkinter import *
from tkinter import messagebox

uid = 'admin'
pw = '1234'
def login():
    username = entry2.get()
    password = entry3.get()
    
    if(username == uid and password == pw):
        messagebox.showinfo("Login Successfull")
    else:
        messagebox.showerror("Login Failed","Invalid Username or Password!")

if(__name__ == '__main__'):
    window = Tk()
    window.title('Login System')
    window.config(background='white')
    window.geometry('300x400')
    
    frame1 = Frame(window)
    frame2 = Frame(window)
    frame3 = Frame(window)
    
    label1 = Label(frame1, text="User login")
    label1.pack(pady=10)
    frame1.pack()
    
    label2 = Label(frame2, text="Username:",bg='white')
    label2.grid(row=0,column=0,pady=5)
    entry2 = Entry(frame2)
    entry2.grid(row=0, column=1, pady=5)
    
    label3 = Label(frame2, text="Password:", bg='white')
    label3.grid(row=0, column=1, pady=5)
    entry3 = Entry(frame2)
    entry3.grid(row=1, column=1, pady=5)
    
    frame2.pack()
    btn_login = Button(frame3, text="Login", width=10,command=login)
    btn_login.pack(pady=15)
    frame3.pack()

    
    window.mainloop()
    