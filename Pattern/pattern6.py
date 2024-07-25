Pattern Question 6:

1 2 3 4 5
1 2 3 4
1 2 3
1 2 
1

Python Solution:

n = int(input("Enter the size of pattern"))

for i in range(n, 0, -1):
    a = 1
    for j in range(i):
        print(a, end=' ')
        a = a + 1
    print()
