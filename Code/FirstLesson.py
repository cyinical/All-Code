import os

def start():
    Name = input('What is your name?\n')
    Age = int(input("What is your age?\n"))
    if Age >= 18:
        print("Hello",Name,"You are legally able to drink in the UK as you are",Age)
        login()
    else:
        print("Hello",Name,"You are not legally able to drink in the UK as you are",Age)
        start()

def login():
    #EUNU means existing user or new user
    EUNU = input("Are you an existing user? Y/N\n")
    if EUNU == "Y" or "y":
        print("Great!")
        userName = 'user'
        passWord = 'password'
        userNameInput = input("Username: ")
        passWordInput = input("Password: ")
        if userName or passWord == userNameInput or passWordInput:
            print('Welcome', userName)
        else:
            print("Does not match")

#elif userNameInput or passWordInput == userName or passWord:
#print("Welcome Calum")

startStop = int(input("Press 1 to start and 0 to stop: "))
if startStop == 1:
    start()
elif startStop == 0:
    os._exit(1)
else:
    print('Invalid')
