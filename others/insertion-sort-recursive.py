
arr = [41, 9, 9, 48, 11, 2, 11, 12, 28, 10, 15, 4, 16, 48]
print(f"Original arr: {arr}")
def insertion_sort_recursive(arr, n):
    if n <= 1:
        return
    insertion_sort_recursive(arr, n-1)
    j = n-1
    i = j-1
    if i>=0 and arr[i]>arr[j]:
        k = i
        key = arr[j]
        while k>=0 and arr[k]>key:
            arr[j] = arr[k]
            j -= 1
            k -= 1
        arr[j] = key
insertion_sort_recursive(arr,len(arr))
print(f"Sorted arr: {arr}")
