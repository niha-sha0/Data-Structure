Pattern Question 8:

*********
 *******
  *****
   ***
    *

Python Solution:
n = int(input("Enter the size of pattern"))

for i in range(n):
    
    for j in range(i):
        print(" ",end='')
    
    for k in range(2*n - (2*i+1)):
        print("*", end='')
    
    for l in range(i):
        print(" ", end='')
            
    print()
