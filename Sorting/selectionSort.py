def selectionSort(arr, n):
    for i in range(n):
        minimum = i 
        for j in range(i+1, n):
            if arr[minimum] > arr[j]:
                minimum = j
                
        arr[i], arr[minimum] = arr[minimum], arr[i]

arr = []
n = int(input("Enter the size of array"))
for i in range(0, n):
    num = int(input(f"Enter the {i}th element"))
    arr.append(num)
    
selectionSort(arr, n)

print("Sorted Array")
for i in range(n):
    print("%d" %arr[i], end=" ")


Time Complexity: O(n^2)
Space Complexity: O(1)
