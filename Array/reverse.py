Reverse an array in-place
Input: [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

Code: 

def reverse(li, n):
    start = 0
    end = n-1
    while start <= end:
        temp = li[start]
        li[start] = li[end]
        li[end] = temp
        start += 1 
        end -= 1 
    print(f"Reversed Array is {li}")

n = int(input("Enter the size of array"))
li = []
for i in range(n):
    num = int(input(f"Enter the {i}th elment"))
    li.append(num)

reverse(li, n)

Time Complexity: O(n)
Space Complexity: O(1)
