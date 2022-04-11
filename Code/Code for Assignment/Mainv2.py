#Python 3
import os
import tkinter as tk
from tkinter import *
window = tk.Tk()

def carSelect():
    #will take to another drop down menu to select model of code
    print("Car") #information will get shown here about different cars
def bikeSelection():
    #will take to another drop down menu to select model of code
    print("Bike") #information will get showen here about different bikes
#checks to see what the selection is in the drop down menu
def Show():
    label = Label(window, text = dropDown.get()).pack()
    if dropDown.get() == "Car":
        carSelect()
    elif dropDown.get() == "Bike": #takes user to bikeSelection
        bikeSelection()
    else:
        #exit the program
        os._exit(1)
optionForCarOrBike = [
    #list of items in the drop down menu
    "Car",
    "Bike",
    "Exit"
    ]
#sets the default to Car
dropDown = StringVar(window)
dropDown.set(optionForCarOrBike[0]) #Tells the drop down menu to default to item 0 in the array
#Selections that allow user to choose
Selection = OptionMenu(window, dropDown, *optionForCarOrBike) #*optionForCarOrBike as it asks for all in the array above to be listed in the drop down
Selection.pack() #Puts it on the screen
selectingButton = tk.Button(text = "Confirm?", command = Show).pack() #When pressed it confirms the order and goes to show to determin answer

window.title('Vehicle Selection') #Sets title
window.geometry('400x400') #Sets size of GUI
window.mainloop()
