def binarySearch(arr, low, high, element):
    while(high >= low):
        mid = low + (high - low) // 2
        
        if arr[mid] == element:
            print(f"The element is found at {mid}th position")
        
        if arr[mid] < element:
            return binarySearch(arr, mid + 1, high, element)
            
        return binarySearch(arr, low, mid - 1, element)

    return -1

def exponentialSearch(arr, n, element):
    if arr[0] == element:
        return 0
    
    i = 1 
    while(i <= n and arr[i] <= element):
        i = i * 2
        
        return binarySearch(arr, i // 2, min(i, n - 1), element)
            
arr = []
n = int(input("Enter the size of the array:"))

for i in range(0, n):
    num = int(input(f"Enter the {i}th element: "))
    
    arr.append(num)
element = int(input("Enter the number to search: "))
exponentialSearch(arr, n, element)


Time Complexity: O(Logn)
Space Complexity: O(1)
