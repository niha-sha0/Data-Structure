def ternarySearch(arr, start, end, element):
    while(end >= start):
        mid1 = start + (end - start) // 3
        mid2 = end - (end - start) // 3
        
        if arr[mid1] == element:
            print(f"The element is found at {mid1}th position")
        if arr[mid2] == element:
            print(f"The element is found at {mid2}th position")
        
        if arr[mid1] > element:
            return ternarySearch(arr, start, mid1 - 1, element)
        elif arr[mid2] < element:
            return ternarySearch(arr, mid2 + 1, end, element)
        else:   
            return ternarySearch(arr, mid1 + 1, mid2 - 1, element)
    return -1
            
arr = []
n = int(input("Enter the size of the array:"))

for i in range(0, n):
    num = int(input(f"Enter the {i}th element: "))
    
    arr.append(num)
element = int(input("Enter the number to search: "))
ternarySearch(arr, 0, n - 1, element)

Time Complexity: O(2 * log3n)
Space Complexity: O(1)

