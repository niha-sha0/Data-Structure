Pattern Question 11:

1
0 1
1 0 1
0 1 0 1
1 0 1 0 1

Python Solution:

n = int(input("Enter the size of pattern"))

for i in range(n):
    flag = 1
    
    if i % 2 == 0:
        flag = 0 
    else:
        flag = 1
        
    for j in range(i):
        print(flag, end='')
        flag = 1 - flag
    print()
