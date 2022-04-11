file = open("stock.csv","a")
userInput = input("Is there Paracetamol left?")
file.write("\n" + userInput)
file.close()
