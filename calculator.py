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
    input("do you like them walm")