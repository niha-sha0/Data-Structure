Pattern Question 10:

*
**
***
****
*****
****
***
**
*

Python Solution:

n = int(input("Enter the size of pattern"))

for i in range(n):
    for j in range(i):
        print("*", end='')
    print()
    
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end='')
    print()
        
