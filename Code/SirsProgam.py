"""
Kevin J Heys

This program is to be used with students as a means of showing them what incorrect programming and formatting looks like.

Students, it is your task to go through this document and correct the errors as well as correct the formatting that you see is incorrect within the code.

You must not use the formatting tool. 
"""

#Libraries to be included within the script.
import tkinter as tk
import os #Operating System for use with Linux and Windows alike.
from tkinter import * #import everything from tkinter library/module.
import csv
import time
from time import sleep

#==========================================================================================================
#DO NOT move OR delete OR change this class!!!!
class Navigating(tk.Tk):
    def __init__(self, *args, **kwargs):

                tk.Tk.__init__(self, *args, **kwargs)#This line of code is extremely important.
                container = tk.Frame(self)
                tk.Tk.wm_title(self, "Python Arduino Number Converter")

                container.pack(side="top", fill="both", expand = True)

                container.grid_rowconfigure(0, weight=1)
                container.grid_columnconfigure(0, weight=1)

                self.frames = {}

        #All classes must be referenced within this for loop
    for F in (StartUp,Binary,Denary,Hexadecimal,DentoHex,DentoBin,BintoDen,BintoHex,HextoDen,HextoBin):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame(StartUp)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
#==========================================================================================================
#As this is the main class, this will be the first thing to come up.
class StartUp(tk.Frame):
    def __init__(self, parent, controller, master=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, master, *args, **kwargs)
        self.master= master

        tk.Label(self,text="Number Converter",font=("Arial",20), fg = "green").place(x=116,y=0)
        tk.Label(self,text="Please choose a conversion type",font=("Arial",15)).place(x=98,y=30)
        Qt = tk.Button(self, text="Quit",command=self.leave, height = 3, width = 5, highlightbackground = "red", fg = "white")
        Qt.place(x=0,y=0)
        Bin = tk.Button(self, text="Binary",command=lambda:               controller.show_frame(Binary), height = 5, width = 20, highlightbackground = "green", fg = "white")
        Bin.place(x=118,y=90)
        Den = tk.Button(self, text="Denary",command=lambda:              controller.show_frame(Denary), height = 5, width = 20, highlightbackground = "green", fg = "white")
        Den.place(x=118,y=190)
        Hex = tk.Button(self, text="Hexadecimal",command=lambda:              controller.show_frame(Hexadecimal), height = 5, width = 20, highlightbackground = "green", fg = "white")
        Hex.place(x=118,y=290)

    def leave(self):
        quit()
#==========================================================================================================

class Binary(tk.Frame):
    def __init__(self, parent, controller, master=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, master, *args, **kwargs)
        self.master= master

        tk.Label(self,text="Number Converter",font=("Arial",20), fg = "green").place(x=116,y=0)
        tk.Label(self,text="You have chosen: Binary",font=("Arial",15)).place(x=119,y=30)
        tk.Label(self,text="What would you like to convert to? : ",                         font=("Arial",15)).place(x=95,y=50)
        Qt = tk.Button(self, text="Quit",command=self.leave, height = 3, width = 5, highlightbackground = "red", fg = "white")
        Qt.place(x=0,y=0)
        Bck = tk.Button(self, text="Menu",command=lambda: controller.show_frame(StartUp), height = 3, width = 5, highlightbackground = "green", fg = "white")
        Bck.place(x=0,y=50)

        #Conversions for this specific method are limited to: Denary and Hexadecimal:
        DenC = tk.Button(self, text="Denary",command=lambda: controller.show_frame(BintoDen), height = 5, width = 20, highlightbackground = "green", fg = "white")
        DenC.place(x=118,y=90)
        HexC = tk.Button(self, text="Hexadecimal",command=lambda: controller.show_frame(BintoHex), height = 5, width = 20, highlightbackground = "green", fg = "white")
        HexC.place(x=118,y=190)


def leave(self):
                    quit()

#===========================================================================================================

class Denary(tk.Frame):
    def __init__(self, parent, controller, master=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, master, *args, **kwargs)
        self.master= master

        tk.Label(self,text="Number Converter",font=("Arial",20), fg = "green").place(x=116,y=0)
        tk.Label(self,text="You have chosen: Denary",font=("Arial",15)).place(x=117,y=30)
        tk.Label(self,text="What would you like to convert to? : ",font=("Arial",15)).place(x=95,y=50)
        Qt = tk.Button(self, text="Quit",command=self.leave, height = 3, width = 5, highlightbackground = "red", fg = "white")
        Qt.place(x=0,y=0)
        Bck = tk.Button(self, text="Menu",command=lambda: controller.show_frame(StartUp), height = 3, width = 5, highlightbackground = "green", fg = "white")
        Bck.place(x=0,y=50)

        #Conversions for this specific method are limited to: Binary and Hexadecimal:
        HexC = tk.Button(self, text="Hexadecimal",command=lambda: controller.show_frame(DentoHex), height = 5, width = 20, highlightbackground = "green", fg = "white")
        HexC.place(x=118,y=90)
        BinC = tk.Button(self, text="Binary",command=lambda: controller.show_frame(DentoBin), height = 5, width = 20, highlightbackground = "green", fg = "white")
        BinC.place(x=118,y=190)


    def leave(self):
                        quit()

#===========================================================================================================

class Hexadecimal(tk.Frame):
    def __init__(self, parent, controller, master=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, master, *args, **kwargs)
        self.master= master

        tk.Label(self,text="Number Converter",font=("Arial",20), fg = "green").place(x=116,y=0)
        tk.Label(self,text="You have chosen: Hexadecimal",font=("Arial",15)).place(x=108,y=30)
        tk.Label(self,text="What would you like to convert to? : ",font=("Arial",15)).place(x=95,y=50)
        Qt = tk.Button(self, text="Quit",command=self.leave, height = 3, width = 5, highlightbackground = "red", fg = "white")
        Qt.place(x=0,y=0)
        Bck = tk.Button(self, text="Menu",command=lambda: controller.show_frame(StartUp), height = 3, width = 5, highlightbackground = "green", fg = "white")
        Bck.place(x=0,y=50)

        #Conversions for this specific method are limited to: Binary and Denary
        DenC = tk.Button(self, text="Denary",command=lambda: controller.show_frame(HextoDen), height = 5, width = 20, highlightbackground = "green", fg = "white")
        DenC.place(x=118,y=90)
        BinC = tk.Button(self, text="Binary",command=lambda: controller.show_frame(HextoBin), height = 5, width = 20, highlightbackground = "green", fg = "white")
        BinC.place(x=118,y=190)


    def leave(
    self):
        quit()

#===========================================================================================================

        classmethod(HextoBin(tk.Frame)):
        def __init__(self, parent, controller, master=None, *args, **kwargs):
            tk.Frame.__init__(self, parent, master, *args, **kwargs)
                        self.master= master

                tk.Label(self,text="Number Converter",font=("Arial",20), fg = "green").place(x=116,y=0)
            tk.Label(self,text="Hexadecimal to Binary",font=("Arial",15)).place(x=128,y=30)
                tk.Label(self,text="1111 is the largest number that can be made",font=("Arial",15)).place(x=78,y=50)
            Qt = tk.Button(self, text="Quit",command=self.leave, height = 3, width = 5, highlightbackground = "red", fg = "white")
                Qt.place(x=0,y=0)
            Bck = tk.Button(self, text="Menu",command=lambda: controller.show_frame(StartUp), height = 3, width = 5, highlightbackground = "green", fg = "white")
                Bck.place(x=0,y=50)
            Bck1 = tk.Button(self, text="Back",command=lambda: controller.show_frame(Hexadecimal), height = 3, width = 5, highlightbackground = "green", fg = "white")
                Bck1.place(x=0,y=100)




    def leave(self):
        quit()

#===========================================================================================================

class HextoDen(tk.Frame):
    def __init__(self, parent, controller, master=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, master, *args, **kwargs)
        self.master= master

        tk.Label(self,text="Number Converter",font=("Arial",20), fg = "green").place(x=116,y=0)
        tk.Label(self,text="Hexadecimal to Denary",font=("Arial",15)).place(x=124,y=30)
        Qt = tk.Button(self, text="Quit",command=self.leave, height = 3, width = 5, highlightbackground = "red", fg = "white")
        Qt.place(x=0,y=0)
        Bck = tk.Button(self, text="Menu",command=lambda: controller.show_frame(StartUp), height = 3, width = 5, highlightbackground = "green", fg = "white")
        Bck.place(x=0,y=50)
        Bck1 = tk.Button(self, text="Back",command=lambda: controller.show_frame(Hexadecimal), height = 3, width = 5, highlightbackground = "green", fg = "white")
        Bck1.place(x=0,y=100)




    def leave(self):
        quit()

#===========================================================================================================

class BintoHex(tk.Frame):
    def __init__(self, parent, controller, master=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, master, *args, **kwargs)
        self.master= master

        tk.Label(self,text="Number Converter",font=("Arial",20), fg = "green").place(x=116,y=0)
        tk.Label(self,text="Binary to Hexadecimal",font=("Arial",15)).place(x=128,y=30)
        Qt = tk.Button(self, text="Quit",command=self.leave, height = 3, width = 5, highlightbackground = "red", fg = "white")
        Qt.place(x=0,y=0)
        Bck = tk.Button(self, text="Menu",command=lambda: controller.show_frame(StartUp), height = 3, width = 5, highlightbackground = "green", fg = "white")
        Bck.place(x=0,y=50)
        Bck2 = tk.Button(self, text="Back",command=lambda: controller.show_frame(Binary), height = 3, width = 5, highlightbackground = "green", fg = "white")
        Bck2.place(x=0,y=100)




    def leave(self):
        quit()

#===========================================================================================================

class BintoDen(tk.Frame):
    def __init__(self, parent, controller, master=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, master, *args, **kwargs)
        self.master= master

        tk.Label(self,text="Number Converter",font=("Arial",20), fg = "green").place(x=116,y=0)
        tk.Label(self,text="Binary to Denary",font=("Arial",15)).place(x=148,y=30)
        Qt = tk.Button(self, text="Quit",command=self.leave, height = 3, width = 5, highlightbackground = "red", fg = "white")
        Qt.place(x=0,y=0)
        Bck = tk.Button(self, text="Menu",command=lambda:[self.destroyEntry(),controller.show_frame(StartUp)], height = 3, width = 5, highlightbackground = "green", fg = "white")
        Bck.place(x=0,y=50)
        Bck2 = tk.Button(self, text="Back",command=lambda:[self.destroyEntry(),controller.show_frame(Binary)], height = 3, width = 5, highlightbackground = "green", fg = "white")
        Bck2.place(x=0,y=100)

        #Main widgets of class start here:
        tk.Label(self,text="Please enter your binary number: ",font=("Arial",15)).place(x=116,y=50)
        global Number
        self.Number = Entry(self,width=30)
        self.Number.place(x=90,y=100)
        conv = tk.Button(self, text="Convert",command= self.Entered, height = 3, width = 10, highlightbackground = "green", fg = "white")
        conv.place(x=148,y=150)

    def Entered(self):
        if(self.Number.get().strip() == "0000"):
            tk.Label(self,text="You have entered: 00 ",font=("Arial",15)).place(x=116,y=260)
                if(self.Number.get().strip() == "0001"):
                    tk.Label(self,text="You have entered: 01 ",font=("Arial",15)).place(x=116,y=260)
                    if(self.Number.get().strip() == "0010"):
                        tk.Label(self,text="You have entered: 02 ",font=("Arial",15)).place(x=116,y=260)
                        if(self.Number.get().strip() == "0011"):
                            tk.Label(self,text="You have entered: 03 ",font=("Arial",15)).place(x=116,y=260)
                            if(self.Number.get().strip() == "0100"):
                                tk.Label(self,text="You have entered: 04 ",font=("Arial",15)).place(x=116,y=260)
                                    if(self.Number.get().strip() == "0101"):
                                            tk.Label(self,text="You have entered: 05 ",font=("Arial",15)).place(x=116,y=260)
                                                if(self.Number.get().strip() == "0110"):
                                                            tk.Label(self,text="You have entered: 06 ",font=("Arial",15)).place(x=116,y=260)
        if(self.Number.get().strip() == "0111"):
            tk.Label(self,text="You have entered: 07 ",font=("Arial",15)).place(x=116,y=260)
        if(self.Number.get().strip() == "1000"):
            tk.Label(self,text="You have entered: 08 ",font=("Arial",15)).place(x=116,y=260)
        if(self.Number.get().strip() == "1001"):
                    tk.Label(self,text="You have entered: 09 ",font=("Arial",15)).place(x=116,y=260)
                if(self.Number.get().strip() == "1010"):
            tk.Label(self,text="You have entered: 10 ",font=("Arial",15)).place(x=116,y=260)
        if(self.Number.get().strip() == "1011"):
                    tk.Label(self,text="You have entered: 11 ",font=("Arial",15)).place(x=116,y=260)
        if(self.Number.get().strip() == "1100"):
                    tk.Label(self,text="You have entered: 12 ",font=("Arial",15)).place(x=116,y=260)
        if(self.Number.get().strip() == "1101"):
                    tk.Label(self,text="You have entered: 13 ",font=("Arial",15)).place(x=116,y=260)
        if(self.Number.get().strip() == "1110"):
                    tk.Label(self,text="You have entered: 14 ",font=("Arial",15)).place(x=116,y=260)
        if(self.Number.get().strip() == "1111"):
                    tk.Label(self,text="You have entered: 15 ",font=("Arial",15)).place(x=116,y=260)

    def destroyEntry(self):
        self.Number.delete(first=0,last=30)
        tk.Label(self,text="                                                                              ",font=("Arial",15)).pl(x=116,y=260)


    def leave(self):
        quit()

    """
    def binArduino(self):
        arduinoData.write('1')
    """

#===========================================================================================================

class DentoBin(tk.Frame):
    def __init__(self, parent, controller, master=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, master, *args, **kwargs)
        self.master= master

        tk.Label(self,text="Number Converter",font=("Arial",20), fg = "green").place(x=116,y=0)
        tk.Label(self,text="Denary to Binary",font=("Arial",15)).place(x=138,y=30)
        tk.Label(self,text="1111 is the largest number that can be made",font=("Arial",15)).place(x=78,y=50)
        Qt = tk.Button(self, text="Quit",command=self.leave, height = 3, width = 5, highlightbackground = "red", fg = "white")
        Qt.place(x=0,y=0)
        Bck = tk.Button(self, text="Menu",command=lambda: controller.show_frame(StartUp), height = 3, width = 5, highlightbackground = "green", fg = "white")
        Bck.place(x=0,y=50)
        Bck3 = tk.Button(self, text="Back",command=lambda: controller.show_frame(Denary), height = 3, width = 5, highlightbackground = "green", fg = "white")
        Bck3.place(x=0,y=100)




    def leave(self):
        quit()

#===========================================================================================================

class DentoHex(tk.Frame):
    def __init__(self, parent, controller, master=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, master, *args, **kwargs)
        self.master= master

        tk.Label(self,text="Number Converter",font=("Arial",20), fg = "green").place(x=116,y=0)
        tk.Label(self,text="Denary to Hexadecimal",font=("Arial",15)).place(x=124,y=30)
        Qt = tk.Button(self, text="Quit",command=self.leave, height = 3, width = 5, highlightbackground = "red", fg = "white")
        Qt.place(x=0,y=0)
        Bck = tk.Button(self, text="Menu",command=lambda: controller.show_frame(StartUp), height = 3, width = 5, highlightbackground = "green", fg = "white")
        Bck.place(x=0,y=50)
        Bck3 = tk.Button(self, text="Back",command=lambda: controller.show_frame(Denary), height = 3, width = 5, highlightbackground = "green", fg = "white")
        Bck3.place(x=0,y=100)




    def leave(self):
        quit()

#===========================================================================================================
#DO NOT CHANGE OR REMOVE!!!!!!!!
root = Navigating()
root.geometry("400x400") #screen sizing - leave it at this do not change it!
root.mainloop() #link to class name to close it.
