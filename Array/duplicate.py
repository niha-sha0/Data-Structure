Duplicate elements in an array
Input: [1, 2, 3, 2, 3]
Output: 2, 3

Code: 
def duplicate(li, n):
    li.sort()
    for i in range(n-1):
        if li[i] == li[i+1]:
            print(f"The duplicate value is {li[i]}")
    return -1

n = int(input("Enter the size of array"))
li = []
for i in range(n):
    num = int(input(f"Enter the {i}th elment"))
    li.append(num)

duplicate(li, n)

Time Complexity: O(nlogn)
Space Complexity: O(1)
