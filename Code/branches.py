#done this is python as I'm not sure how to do it in C
while[1]:
    weight = int(input("Please input the weight: "))
    if weight < 50:
        print("Your price is £6.60")
    elif weight < 100:
        print("your price is £15")
    elif weight < 1000:
        print("your price is £50")
    else:
        print("The weight is too heavy")

