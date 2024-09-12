Second Largest Number
Input: [1, 2, 3, 4, 5]
Output: 4

Code:

def largest(li, n):
    first = li[0]
    sec = li[0]
    for i in range(n):
        if first < li[i]:
            sec = first
            first = li[i]
        elif sec < li[i]:
            sec = li[i]
    print(f"The second largest no. is {sec}")

n = int(input("Enter the size of array"))
li = []
for i in range(n):
    num = int(input(f"Enter the {i}th elment"))
    li.append(num)

largest(li, n)

Time Complexity: O(n)
Space Complexity: O(n)
