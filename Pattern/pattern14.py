Pattern Question 14:

A
A B
A B C
A B C D
A B C D E

Pattern Solution:

n = int(input("Enter the size of pattern"))

str = ord('A')
for i in range(1, n):
    s = str
    for j in range(1, i):
        print(chr(s+j-1), end=' ')
    print()
