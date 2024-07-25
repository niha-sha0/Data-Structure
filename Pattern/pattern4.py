Pattern Question 4:

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

Python Solution:

n = int(input("Enter the size of pattern"))

for i in range(n):
    for j in range(i):
        print(i,end=' ')
    print()
