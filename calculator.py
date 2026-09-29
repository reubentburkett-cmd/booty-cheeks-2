print("calculator of doom the sprickulator")
input1 = input("code word: ")
if input1 == 'calculator':
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
    input2 = input("do you like them hot: ")
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
                print('then take your baby put it on the fring pan for twenty minutes, and add some salt and pepper to it')
                print('then wizz it up in a blender for 20 secons')
                input7 = input('want to make it a milkshake: ')
                if input7 == 'yes':
                    print('then toss it in the wizzer with some ice cream and milk for a cople of seconds and bam a baby flavored milkshake')
                if input7 == 'no':
                    print('then a soup it is, toss it in a blender with some vegtables and spices maybe some salt if you want put it all in a pot and let it cook for therty minutes to an hour and bam now you have made baby soup')
            if input6 == 'no':
                input11 = input('want to add it to a mc meal: ')
                if input11 == 'yes':
                    print('then put it in a bun add some scliced up pickles, tomato suoce, and a sclice of cheese, and bam your mc baby is ready(it gos realy well with the mc baby friys)')
        if input5 == 'no':
            print('then body temp it is')
            input8 = input('want to chop up the baby: ')
            if input8 == 'yes':
                print('then chop it up into thin little stack chops')
                input9 = input('want to put it in the deep frier: ')
                if input9 == 'no':
                    print('then where going to make a baby salad, toss the baby in the oven to cook for fourty minutes, while the baby is cooking chop up some vegtables for the salad, once the baby stops cooking and is at the disiered temp, bring it out of the oven and put it with the choped up vegtables, and to finish it off, add a nice dresing to it and your done, enjoy your baby salad')
                if input9 == 'yes':
                    print('then put it in the deep frier for five minutes, once its all crispy(by the way this meal gos well with the mc baby), grab some tomato souce and your done have fun eating your mc baby fris')
            if input8 == 'no':
                print('then stuff your baby with fruit paste')
                input10 = input('want to put it in the deep frier: ')
                if input10 == 'yes':
                    print('then toss it in the deep frier for five minutes, when done ad some scorse on it and enjoy your baby tart ')