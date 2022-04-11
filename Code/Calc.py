while(1):
    input1 = int(input('First number: '))
    val = input('-,+,*,/: ')
    input2 = int(input('Second number: '))

    if val == '+':
        output = input1 + input2
        print(output)

    if val == '-':
        if input2 > input1:
            output = input2 - input1
            print(output)
        else:
            output = input1 - input2
            print(output)

    if val == '*':
        output = input1 * input2
        print(output)

    if val == '/':
        if input2 > input1:
            output = input2 / input1
            print(output)
        else:
            output = input1 / input2
            print(output)
