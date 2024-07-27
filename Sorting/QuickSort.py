def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
        
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

arr = []
n = int(input("Enter the size of array"))
for i in range(0, n):
    num = int(input(f"Enter the {i}th element"))
    arr.append(num)
quickSort(arr, 0, n-1)

print("Sorted Array")
for i in range(n):
    print("%d" %arr[i], end=" ")

Time Complexity: O(nlogn)
Space Complexity: O(1)
