class FirstClass:
    y = 'Hello there, this is from first class'
class SecondClass:
    first = FirstClass()
    #Cannot say print y as its in a seperate class.
    print(first.y)
    print('This is from second class')
