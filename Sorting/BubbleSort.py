def bubbleSort(arr, n):
    for i in range(n):
        sorted = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                sorted = True
        if sorted == False:
            break

arr = []
n = int(input("Enter the size of array"))
for i in range(0, n):
    num = int(input(f"Enter the {i}th element"))
    arr.append(num)
    
bubbleSort(arr, n)

print("Sorted Array")
for i in range(n):
    print("%d" %arr[i], end=" ")

Time Complexity: O(n^2)
Space Complexity: O(1)
