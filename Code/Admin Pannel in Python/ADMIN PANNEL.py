#python 3
import os
import tkinter as tk
from tkinter import *
window = tk.Tk()
#Start of code

#declaring it a string
usernameText = StringVar() #Sets it as a string
passwordText = StringVar() #Sets it as a string

#label and entry for username and password
usernameLabel = Label(text = "Username:").pack() #.pack() puts it on the screen
usernameEntry = Entry(textvariable = usernameText).pack() 
passwordLabel = Label(text = "Password:").pack()
passwordEntry = Entry(textvariable = passwordText).pack()

#Reading from Usernames and Passwords
usernameTextFile = open("Usernames.txt","r")
for line in usernameTextFile:
    usernameLine = usernameTextFile.readlines()
passwordTextFile = open("Passwords.txt","r")
for line in passwordTextFile:
    passwordLine = passwordTextFile.readlines()

#checking if the tests from files to text are same as inputted
def CHECK():
    if usernameText == usernameLine and passwordText == passwordLine:
        print("Login sucsesful")
    else:
        print("Login unsucsessful")

#buttons
signinButton = Button(text = "Sign-in", command = CHECK).pack()
#End of code
window.title('Admin Pannel') #Sets title
window.geometry('400x400') #Sets size of GUI
window.mainloop()
