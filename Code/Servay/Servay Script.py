#python 3
import os
import webbrowser
#import smtplib
import tkinter as tk
from tkinter import *
#from tkinter import ttk
window = tk.Tk()
#Code goes here:

def saveAll():
    artistInfo = first.get()
    ageInfo = second.get()
    ageInfo = str(ageInfo)
    gameCompetedInfo = third.get()
    completedGame = fourth.get()
    #print(artistInfo, ageInfo, gameCompetedInfo, completedGame)
    saveInfo = open("USERINFO.txt","w")
    saveInfo.write(artistInfo)
    saveInfo.write("\n")
    saveInfo.write(ageInfo)
    saveInfo.write("\n")
    saveInfo.write(gameCompetedInfo)
    saveInfo.write("\n")
    saveInfo.write(completedGame)
    saveInfo.close()
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    
def closeProgram():
    os._exit(0)

#entries in string and intager form
first = StringVar()
second = IntVar()
third = StringVar()
fourth = StringVar()

artistLabel = Label(text = "What is your favourite artist?").pack()
artistEntry = Entry(textvariable = first).pack()
personsAge = Label(text = "How old are you?").pack()
personsAgeEntry = Entry(textvariable = second).pack()
gameCompleted = Label( text = "Have you ever fully completed a game before?").pack()
gameCompletedEntry = Entry(textvariable = third).pack()
completed = Label(text = "What was the first game you completed?").pack()
completedEntry = Entry(textvariable = fourth).pack()

enterAllButton = Button(window, text = "Save Info to text file", command = saveAll).pack()
closeButton = Button(window, text = "Close", bg = "Red", fg = "White", command = closeProgram).pack()

window.title('Servey') #Sets title
window.geometry('400x400') #Sets size of GUI
window.mainloop()
