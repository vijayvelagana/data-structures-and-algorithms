
arr = [41, 9, 9, 48, 11, 2, 11, 12, 28, 10, 15, 4, 16, 48]
print(f"Original arr: {arr}")
def bubble_sort_recursive(arr, n):
    if n <= 1:
        return
    for i in range(n):
        j = i+1
        if j<n and arr[i]>arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
    bubble_sort_recursive(arr, n-1)
bubble_sort_recursive(arr,len(arr))
print(f"Sorted arr: {arr}")
