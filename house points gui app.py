#import 
 
from tkinter import *
import os
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()

# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def incorrect_login():
    global incorrect_login_screen
    incorrect_login_screen= Toplevel(login_screen)
    incorrect_login_screen.title("Success")
    incorrect_login_screen.geometry("150x100")
    Label(incorrect_login_screen, text="Invalid Password or Login Id ").pack()
    Button(incorrect_login_screen, text="OK", command=delete_incorrect_login).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    if username1=="a" and password1=="b":
        login_sucess() 
    else:
        incorrect_login()
 

 
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_incorrect_login():
    incorrect_login_screen.destroy()
  
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    main_screen.mainloop()
 
 
main_account_screen()
