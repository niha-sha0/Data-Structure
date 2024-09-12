Find the number of even and odd integers in a given array of integers.
Input: [1, 2, 3, 4, 5]
Output: Even = 2
        Odd = 3

Code: 

def evenOdd(input_list, n):
    even = 0
    odd = 0
    for i in range(n):
        if li[i] % 2 == 0:
            even += 1 
        else:
            odd += 1 
    print(f"No. of even elements are {even}")
    print(f"No. of odd elements are {odd}")
    
n = int(input("Enter the size of array"))
li = []
for i in range(n):
    num = int(input(f"Enter the {i}th elment"))
    li.append(num)

evenOdd(li, n)

Time Complexity: O(n)
Space Complexity: O(1)
