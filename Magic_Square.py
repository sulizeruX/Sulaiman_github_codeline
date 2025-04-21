num_input = input("intput a number")

# while type(num_input) != int:
#     input("input a f*&king number you dolt")
# else:
num = int(num_input)
table = [[0]*num for _ in range(num)]
for i in range(num*num):
    total = num*num
    remainder = (i/num)
    num1 = (total - i + (2*int(remainder)))%num
    num2 = (i)%num - int(remainder)
    table[num1][num2] = i + 1
    for j in range(num):
        print(str(table[j]).replace("[", "").replace("]", "").replace('"', '').replace(",", ""))
    print()
    