Pattern Question 13:

1             1
1 2         2 1
1 2 3     3 2 1  
1 2 3 4 4 3 2 1

Python Solution:

n = int(input("Enter the size of pattern: "))

for i in range(1, n):
    for j in range(i):
        print(j+1, end=' ')
    for k in range(1,2*(n-i)-1):
        print(" ",end=' ')
    for l in  range(i-1, -1, -1):
        print(l+1, end=' ')
    print()
