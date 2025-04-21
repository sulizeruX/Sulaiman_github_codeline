import time

strike = 0

num1 = input("input the first number or else: \n")

while not num1.isnumeric():
    num1 = input("I SAID PUT A NUMBER!!!!!!!!!: \n")
    strike += 1

num2 = input("now don't you play with me, if I don't see a second number, I promise I will rip out your soul: \n")

while not num2.isnumeric():
    num2 = input("(whisper's)I am holding you a gun point, PICK A NUMBER!!!!!!! \n: ")
    strike += 1

operation = input("now choose plus or minus: \n")

while operation != "+" or operation != "-":
    strike += 1
    if strike >= 3:
        print("that is it, I AM GONNA DESTROY YOUR LAPTOP NOW!!!! \n in 5 seconds that is")
        time.sleep(5)
        print("YOU DID THIS!!!!!! \nw" * 10)
        break
    else:
        operation = input("don't you play with me, IT'S A SIMPLE PLUS OR MINUS: \n")

if operation == "+":
    result = int(num1) + int(num2)
    print(num1 + "+" + num2 + "=" + result)
elif operation == "-":
    result = int(num1) - int(num2)
    print(num1 + "-" + num2 + "=" + result)

