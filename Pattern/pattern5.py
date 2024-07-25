Pattern Question 5:

* * * * *
* * * *
* * * 
* *
*

Python Solution:

n = int(input("Enter the size of pattern"))

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=' ')
    print()
