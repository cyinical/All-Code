#import webbrowser
#import time
Rooms = [1,2,3,4]
Dates = []
Names = []
roomTaken = []
def BookingRoom():
    print("These are current rooms available to Let:", Rooms)
    takeRoom = int(input('Type the room number you wish to book: '))
    #checks if user input is a room thats in the list
    if takeRoom in Rooms:
        dayInput = int(input("Please input the day you wish to take: "))
        monthInput = int(input("Please input the moneht you wish to take: "))
        nameInput = input("Please add a name to this room: ").upper()
        print("You have scedualed room",takeRoom,"on the date",dayInput,monthInput,"2022. This room is booked by",nameInput)
        #Rooms.pop(takeRoom - 1) not needed
        print(Rooms,"are left avalable")
        roomTaken.append(takeRoom)
        Dates.append(dayInput)
        Dates.append(monthInput)
        Names.append(nameInput)
        print(takeRoom,"by",nameInput,"on the date",dayInput,"/",monthInput,"/","2022")
        Final = input("Is this information correct? Y/N: ").upper()
        if Final == "Y":
            Total = "Room",takeRoom,"taken by",nameInput,"on",dayInput,"/",monthInput,"."
            writeNewTotal = str(Total)
            writeTotal = open(takeRoom,"a")
            wT = writeTotal
            wT.write(writeNewTotal)
            wT.close()
        else:
            #this was just something funny, all it does is check if the name is equal to rick and rick rolls people
            #if nameInput == "RICK":
                #webbrowser.open("https://www.youtube.com/watch?v=rTgj1HxmUbg", new=1)
            #this part of the code is nothing to do with rick rolling
            print("Cancelled")
            BookingRoom()
    else:
        print("This room does not exist/taken",Rooms,"are available")
#Start
while[1]:
    askingRoom = input("Are you looking to book a room? Y/N/EXIT: ").upper()
    if askingRoom == "Y":
        BookingRoom()
    elif askingRoom == "N":
        print("Not Pog")
    elif askingRoom == "EXIT":
        exit(1)
    else:
        pass
