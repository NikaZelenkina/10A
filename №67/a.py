from random import *

n,m=5,4
a= [[randint(10,99) for j in range(m)] for i in range(n)]


for i in range(n):
    for j in range(m):
        print("{:4d}".format(a[i][j]), end = " ")
    print()

max_item=  10

min_item= 99


for i in range(n):
    for j in range(m):
        if a[i][j]> max_item:
            max_item = a[i][j]
print("ьфксимальное число",(max_item))

for i in range(n):
    for j in range(m):
        if a[i][j]< min_item:
            min_item = a[i][j]
print("минимальное число",(min_item))


