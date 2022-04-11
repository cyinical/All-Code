roomType = [
    "SINGLE",
    "DOUBLE"
    ]

paymentMethod = [
    "Paypal",
    "Debit"
    ]
'''
print("B&B")
askRoom = input("Would you like a Single or Double").upper()
if askRoom == roomType:
    print("£20")
elif askRoom == roomType:
    print("£40")
else:
    ("Invalid")
'''
#-----------------------------------------------------------
#python 3
#import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
window = tk.Tk()
#Start of code

Label(text = "B&B", bg = "blue", fg = "white", font = 20).pack()
roomSelect = ttk.Combobox(value = roomType, font = 20)
roomSelect.current(0)
roomSelect.pack()
paymentSelect = ttk.Combobox(value = paymentMethod, font = 20)
paymentSelect.current(0)
paymentSelect.pack()

#End of code
window.title('Bed & Breakfast') #Sets title
window.geometry('400x400') #Sets size of GUI
window.mainloop()
