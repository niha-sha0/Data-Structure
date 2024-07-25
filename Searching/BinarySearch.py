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
