def readFile():
    file = open("writingFile.txt", "r")
    for line in file:
        print(line, end = '')
    file.close()

def writeFile():
    file = open("writingFile.txt", "w")
    file.write('Thanks for the invite, see you there\n')
    file.close


def appendFile():
    askUserIfInput = input('Would you like to add to the file? y/n\n')
    if askUserIfInput == 'n':
        pass
    else:
        print('Please enter what you want to say:')
        file = open("writingFile.txt", "a")
        userInput = input('')
        file.write(userInput)
        file.close()
def xFile():
    #Using x, x makes files
    print('Name a file!')
    userInput = input('')
    userInput = userInput+".txt"
    file = open(userInput, "x")
    file.close()
    
writeFile()
readFile()
appendFile()
xFile()
