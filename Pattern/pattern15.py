Pattern Question 15:

A B C D E
A B C D
A B C
A B
A

Pattern Solution:

n = int(input("Enter the size of pattern"))

str = ord('A')
for i in range(1, n):
    s = str
    for j in range(1, n-i+1):
        print(chr(s+j-1), end=' ')
    print()
