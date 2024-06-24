Pattern question 1:

* * * * *
* * * * *
* * * * * 
* * * * *
* * * * *


Solution in Python 

n = int(input("Enter the size of pattern"))

for i in range(n):
    for j in range(n):
        print("* ",end='')
    print()
