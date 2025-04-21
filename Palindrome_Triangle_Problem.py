print("enter number of rows for the triangle")
# n = int(input())
n = int(input())
x = [0] * (n * 2 - 1)
# x = [" "] * (n * 2 - 1)
index_1 = n - 1
index_2 = n - 1
for i in range(len(x) * n):
    if i%len(x) >= index_1 and i%len(x) <= index_2:
        x[i%len(x)] = x[i%len(x)] + 1
    if i%len(x) == len(x) - 1:
        index_1 -= 1
        index_2 += 1
        s = str(x).replace(",", "").replace("[", "").replace("]", "").replace("'", "").replace("0", "")
        print(s)
        # print(x)
# for i in range(n):
#     if i == 0:

#     else:

