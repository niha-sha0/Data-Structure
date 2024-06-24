Pattern Question 3:

1 
1 2
1 2 3 
1 2 3 4
1 2 3 4 5

Python Solution: 

n = int(input("Enter the size of pattern"))

for i in range(n):
    a = 1
    for j in range(i):
        print(a,end=' ')
        a = a + 1
    print()
