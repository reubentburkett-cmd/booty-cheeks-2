print("couculator of doom the sprickulator")
input1 = input("code word: ")
if input1 == 'culator':
    num1 = input("number 1: ")
    val = input("opreator: ")
    num2 = input("number 2:")
    num1 = int(num1)
    num2 = int(num2)
    if val == "+":
        ans = num1 + num2
    elif val == "-":
        ans = num1 - num2
    elif val == "/":
        ans = num1 / num2
    elif val == "*":
        ans =num1 * num2
    print(ans)
elif input1 == 'baby':
    print("how do you like you baby")
    input2 = input("do you like them walm: ")
    if input2 == 'yes':
        print("then toss it in the microwave for 30 seconds")
        input3 = input('want it to be roasted: ')
        if input3 == 'yes':
            print('put it in the oven for an hour on low')
            input4 = input('want to make it a disert: ')
            if input4 == 'yes':
                print('then put it in a bowl with ice cream and enjoy your tasty baby disert')
    if input2 == "no":
        input5 = input("then do you want it cold: ")
        if input5 == "yes":
            print('then toss it in the frezer for one day and start to unfreze it the nexst day')
            input6 = input('want to wizz it up in a blender: ')
            if input6 == 'yes':
                print('then wizz it up in a blender for 20 secons')
                input7 = input('want to make it a milkshake: ')
                if input7 == 'yes'