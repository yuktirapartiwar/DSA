# WAP to search an element in a sorted matrix

n = 4 # no. of rows
m = 5 # no. of columns

a = [[0, 6, 8, 9, 11],
     [20, 22, 28, 29,31],
     [36, 38, 50, 61, 63],
     [64, 66, 100, 122, 128]]

k = 128 # element to search
flag = 0

for i in range(0, n):
    for j in range(0, m):
        if (a[i][j] == k):
            print(k, " found at position (", i, ", ", j, ")")
            flag = 1

if (flag == 0):
    print("Element not Found.")