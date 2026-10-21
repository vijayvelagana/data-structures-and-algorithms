
# Bubble Sort (Adjacent Swap)

nums = [5, 8, 1, 6, 9, 2, 4]
print(f"Original nums: {nums}")
n = len(nums)
for count in range(n):
    is_swapped = False
    for i in range(n):
        j = i+1
        if j<n and nums[i] > nums[j]:
            # Swap
            nums[i], nums[j] = nums[j], nums[i]
            is_swapped = True
    if not is_swapped:
        break # Already in sorted
print(f"Sorted nums: {nums}")
# Time complexity = O(N**2)
# Space complexity = O(1)
