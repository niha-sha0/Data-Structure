Pattern question 2:

*
* *
* * *
* * * * 
* * * * *

Python Solution:

n = int(input("Enter the size of pattern"))

for i in range(n):
    for j in range(i):
        print("* ",end='')
    print()
