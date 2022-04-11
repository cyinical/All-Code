import os
x = 0
z = 1
while x != 1:
    shutOff = input("Don't press E: ")
    shutOffNew = shutOff.upper()
    print(shutOffNew + ". This is attempt:",z)
    if len(shutOffNew) > 2:
        print('Error! Only one letter!')
    #adds one to the counter
    z = z + 1
    if shutOffNew == 'E':
        x = x + 1
        os._exit(1)
    
