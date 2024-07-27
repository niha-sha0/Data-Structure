def insertionSort(arr, n):
    for i in range(n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
            
        arr[j+1] = key

arr = []
n = int(input("Enter the size of array"))
for i in range(0, n):
    num = int(input(f"Enter the {i}th element"))
    arr.append(num)
    
insertionSort(arr, n)

print("Sorted Array")
for i in range(n):
    print("%d" %arr[i], end=" ")


Time Complexity: O(n^2)
Space Complexity: O(1)
