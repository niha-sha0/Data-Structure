Pattern Question 12:

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

Python Solution:

n = int(input("Enter the size of pattern"))
ans = 1
for i in range(n):
    for j in range(i):
        print(ans, end=' ')
        ans = ans + 1
    print()
