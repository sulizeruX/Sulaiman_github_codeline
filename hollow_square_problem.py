print("enter number of rows and columns")
n = int(input())
for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")
        # print("*" + " " * (n - 2) + "*")