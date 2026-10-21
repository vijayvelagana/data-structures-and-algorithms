

# Merge Sort (Divide and Merge)
arr = [3, 1, 2, 4, 1, 5, 2, 6, 4]
n = len(arr)
def merge_sort(start, end, arr):
    if start == end:
        return [arr[start]]
    mid = (start+end) // 2
    left = merge_sort(start, mid, arr)
    right = merge_sort(mid+1, end, arr)
    i, j = 0, 0
    temp = []
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
    while i<len(left):
        temp.append(left[i])
        i += 1
    while j<len(right):
        temp.append(right[j])
        j += 1
    return temp
    

print(f"Original arr: {arr}")
sorted_arr = merge_sort(0, n-1, arr)
print(f"Sorted arr: {sorted_arr}")

# Time complexity = O(logN * N)
# Space complexity = O(N + logN) = O(N) (logN) is recursion stack space

