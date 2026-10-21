
arr = [5, 3, 8, 4, 2, 7, 1, 10]
print(f"Original arr: {arr}")

def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while True:
        while i<=high and arr[i] <= pivot: # find greater than pivot 
            i += 1
        while arr[j] > pivot: # find lesser than or equal to pivot
            j -= 1
        if i>=j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_sort(arr, low, high):
    if low >= high:
        return
    p = partition(arr, low, high)
    quick_sort(arr, low, p-1)
    quick_sort(arr, p+1, high)
    
quick_sort(arr, 0, len(arr)-1)
print(f"Sorted arr: {arr}")
