Find the common elements between two arrays (string, integer, etc.) of sorted elements.

Input: list1 = [1, 2, 3, 4, 5]
       list2 = [3, 4, 5, 6]

Output: [3, 4, 5]

Code: 
def commonElements(list1, list2, m, n):
    for i in range(m):
        for j in range(n):
            if list1[i] == list2[j]:
                print("Commond elements are")
                print(list1[i], end=" ")
    return -1

m = int(input("Enter the size of array"))
n = int(input("Enter the size of array"))
list1 = []
for i in range(m):
    num = int(input(f"Enter the {i}th elment"))
    list1.append(num)
    
list2 = []
for i in range(n):
    num = int(input(f"Enter the {i}th elment"))
    list2.append(num)

commonElements(list1, list2, m, n)

Time Complexity: O(n^2)
Space Complexity: O(1)
