tn=input("Enter a team name ")
print("Welcome to the quiz",tn)
def choose():
     quiz=["1","2"]
     choice=input("type in 1 or two for quiz and anything else to quit")
     if choice==quiz[0]:
        numbers()
     elif choice==quiz[1]:
        alpha()
     else:
        exit()

def numbers():
    questions=["one","two","three","four","five","six"]
    x=0

    while (x!=6):
        print("Type",questions[x])
        q1=input("")
        if q1==questions[x]:
            print("correct")
            x+=1

        else:
            exit()
    print("You can type numbers yay!")
    choose()

def alpha():
    questions=["alphabet","A number","IamInPain","help","me","plz"]
    x=0

    while (x!=6):
        print("Type",questions[x])
        q1=input("")
        if q1==questions[x]:
            print("correct")
            x+=1

        else:
            exit()
    print("You can type yay!")
    choose()



choose()
