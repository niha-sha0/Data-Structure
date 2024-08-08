def interpolationSearch(arr, low, high, element):
    if(low <= high and element >= arr[low] and element <= arr[high]):
        pos = low + (((element - arr[low])//(arr[high]-arr[low])) * (high - low))
        
        if arr[pos] == element:
            print(f"The element is found at {pos}th position")
        
        if arr[pos] < element:
            return interpolationSearch(arr, pos + 1, high, element)
        interpolationSearch(arr, low, pos - 1, element)
            
    return -1        
            
arr = []
n = int(input("Enter the size of the array:"))

for i in range(0, n):
    num = int(input(f"Enter the {i}th element: "))
    
    arr.append(num)
element = int(input("Enter the number to search: "))
interpolationSearch(arr, 0, n - 1, element)

Time Complexity: O(log2(log2 n)) for average case, O(n) for worst case
Space Complexity: O(1)
