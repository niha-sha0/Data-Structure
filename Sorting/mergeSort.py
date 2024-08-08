def merge(arr, l, m, r): 
    left = arr[l : m+1]
    right = arr[m+1 : r+1]
            
    i = 0
    j = 0
    k = l
        
    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            arr[k] = left[i]
            i +=1
            k +=1
        else:
            arr[k] = right[j]
            j +=1
            k +=1
    while i < len(left):
        arr[k] = left[i]
        i +=1
        k +=1
    while j < len(right):
        arr[k] = right[j]
        j +=1
        k +=1
        
def mergeSort(arr, l, r):
        
    if l >= r:
        return 
    m = (l+r) // 2
        
    mergeSort(arr, l, m)
    mergeSort(arr, m+1, r)
            
    merge(arr, l, m, r)
        
arr = []
n = int(input("Enter the size of array"))
for i in range(0, n):
    num = int(input(f"Enter the {i}th element"))
    arr.append(num)
mergeSort(arr, 0, n-1)

print("Sorted Array")
for i in range(n):
    print("%d" %arr[i], end=" ")
    
Time Complexity: O(nlogn)
Space Complexity: O(n)
