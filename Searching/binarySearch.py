Using Iterative Approach:

def binarySearch(arr, n, element):
    start = 0
    end = n - 1
    while(start <= end):
        mid = start + (end - start) // 2
        
        if arr[mid] == element:
            print(f"The element is found at {mid}th position")
        
        if arr[mid] < element:
            start = mid + 1
        else:
            end = mid - 1
            
    return -1
arr = []
n = int(input("Enter the size of the array:"))

for i in range(0, n):
    num = int(input(f"Enter the {i}th element: "))
    
    arr.append(num)
element = int(input("Enter the number to search: "))
binarySearch(arr, n, element)

Time Complexity: O(logn)
Space Complexity: O(1)


Using Recursive Approach:

def binarySearch(arr, n, start, end, element):
    if(end >= start):
        mid = start + (end - start) // 2
        
        if arr[mid] == element:
            print(f"The element is found at {mid}th position")
        
        if arr[mid] < element:
            return binarySearch(arr, n, mid + 1, end, element)
        binarySearch(arr, n, start, mid - 1, element)
            
arr = []
n = int(input("Enter the size of the array:"))

for i in range(0, n):
    num = int(input(f"Enter the {i}th element: "))
    
    arr.append(num)
element = int(input("Enter the number to search: "))
binarySearch(arr, n, 0, n - 1, element)
