print("Hello! This is a fact file about me, if you knew the fact I will give\nplease answer Yes or No\n")

myName = 'My name is Calum, did you know this\n'
myAge = '\nMy age is 19\n'

file = open("facts.txt","w")
print(myName)
userInputName = input('Did you know this? ')
file.write(myName)
file.write(userInputName)
print(myAge)
userInputAge = input('Did you know this? ')
file.write(myAge)
file.write(userInputAge)
file.close()
