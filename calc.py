import time

def power(num1, num2):
    result = 0
    for i in range(num2):
        result = result * num1
    print(num1 + " to the power of " + num2 + " is " + result)

def factorial(num1):
    result = 0
    for i in range(num1):
        result = result * (num1 - i)
    print("the factorial of " + num1 + " is " + result)

def absolute(num1):
    print(abs(num1))

strike = 0

num1 = input("input the first number or else: \n")

while not num1.isnumeric():
    num1 = input("I SAID PUT A NUMBER!!!!!!!!!: \n")
    strike += 1

num2 = input("now don't you play with me, if I don't see a second number, I promise I will rip out your soul \n or you could type 'f' for factorial or 'a' for absolute value of your first number:) :\n")

while (not num2.isnumeric()) or num2 != "f" or num2 != "a":
    num2 = input("(whisper's in the ear)I am holding you a gun point\nPICK A NUMBER NOW!!!!!!! \n: ")
    strike += 1

if num2 == "f":
    factorial(num1)
elif num2 == "a":
    absolute(num1)
else:
    operation = input("now choose +, -, *, /, power, OR, AND, or XOR: \n")

    while operation != "+" or operation != "-" or operation != "*" or operation != "/" or operation != "power" or operation != "OR" or operation != "AND" or operation != "XOR":
        strike += 1
        if strike >= 3:
            print("that is it, I AM GONNA DESTROY YOUR LAPTOP NOW!!!! \n you have 10 seconds to say bye to your laptop\n")
            time.sleep(10)
            print("YOU DID THIS!!!!!! \n" * 1000)
            break
        else:
            operation = input("don't you play with me, IT'S A SIMPLE CHOICE!!!!\n +, -, *, /, POWER(in small letters of course), OR, AND, or XOR!!!!!!!! :\n")

    if operation == "+":
        result = int(num1) + int(num2)
        print(num1 + "+" + num2 + "=" + result)
    elif operation == "-":
        result = int(num1) - int(num2)
        print(num1 + "-" + num2 + "=" + result)
    elif operation == "*":
        result = int(num1) * int(num2)
        print(num1 + "*" + num2 + "=" + result)
    elif operation == "/":
        result = int(num1)/int(num2)
        print(num1 + "/" + num2 + "=" + result)
    elif operation == "power":
        power(num1, num2)
    elif operation == "OR":
        print(num1 | num2)
    elif operation == "AND":
        print(num1 & num2)
    elif operation == "XOR":
        print(num1 ^ num2)