def linearSearch(arr, n, element):
    for i in range(n):
        if arr[i] == element:
            print(f"The element is found at {i}th position")
    return -1

arr = []
n = int(input("Enter the size of the array:"))

for i in range(0, n):
    num = int(input(f"Enter the {i}th element: "))
    
    arr.append(num)
element = int(input("Enter the number to search: "))
linearSearch(arr, n, element)

Time Complexity: O(n)
Space Complexity: O(1)
