Pattern Question 16:

A
B B
C C C 
D D D D
E E E E E

Pattern Solution:

n = int(input("Enter the size of pattern"))

str = ord('A')
s = str
for i in range(1, n):
    for j in range(i):
        print(chr(s), end=' ')
    
    s = s+1    
        
    print()
