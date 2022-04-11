import os
symbols = ['addition','subtract','multiply','division','exit']

while[1]:
    def Input():
        global userInput
        userInput = input('Please select one of the following:\nAddition\nSubtract\nMultiply\nDivision\nExit\n').lower()
    Input()
    checkInput = input('Was that correct? Y/N\n').upper()
    #if it's wrong, go back
    if checkInput == 'N':
        Input()

    def Exit():
        #stop the program
        os._exit(1)
    
    fisrtNumber = int(input('Enter First Number: '))
    secondNumber = int(input('Enter Second Number: '))

#this is all +,-,*,/    
    def Addition():
        answer1 = fisrtNumber + secondNumber
        print(answer1)

    def Subtract():
        if fisrtNumber < secondNumber:
            answer2 = secondNumber - fisrtNumber
            print(answer2)
        else:
            answer2 = fisrtNumber - secondNumber
            print(answer2)

    def Multiply():
        answer3 = fisrtNumber * secondNumber
        print(answer3)

    def Division():
            answer4 = secondNumber / fisrtNumber
            print(answer4)
#check user input
    if userInput == symbols[0]:
        Addition()

    if userInput == symbols[1]:
        Subtract()

    if userInput == symbols[2]:
        Multiply()

    if userInput == symbols[3]:
        Division()

    if userInput == symbols[4]:
        Exit()

