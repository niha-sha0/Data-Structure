Pattern Question 7:

     *
    ***
   *****
  *******
 *********

Python Solution:

n = int(input("Enter the size of pattern"))

for i in range(n, 0, -1):
    
    for j in range(i-1):
        print(" ",end='')
    
    for k in range(n-i):
        for l in range(k):
            print("*", end='')
    print()
