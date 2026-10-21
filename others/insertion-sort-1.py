

# Insertion Sort

arr = [3, 5, 6, 4, 8, 9, 10, 7, 1]
print(f"Original arr: {arr}")
n = len(arr)
for i in range(n):
    j = i+1
    if j < n and arr[i] > arr[j]:
        ele = arr[j]
        k = i
        while arr[k] > ele:
            k -= 1
        arr.pop(j) # O(N)
        arr.insert(k+1, ele) # O(N)
print(f"Sorted arr: {arr}")

# Time complexity = O(N**2)
# Space complexity = O(1)
