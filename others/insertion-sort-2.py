

# Insertion Sort

arr = [3, 5, 6, 4, 8, 9, 10, 7, 1]
print(f"Original arr: {arr}")
n = len(arr)
for i in range(n):
    j = i+1
    if j<n and arr[i]>arr[j]:
        k = i
        ele = arr[j]
        while k>=0 and arr[k] > ele:
            arr[j] = arr[k]
            k -= 1
            j -= 1
        arr[j] = ele
print(f"Sorted arr: {arr}")

# Time complexity = O(N**2)
# Space complexity = O(1)
