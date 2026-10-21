# kadane's Algorithm
# Find max sub array sum in a given bytearray

class Solution:
    def get_max_subarray_sum(self, nums):
        res = float('-inf')
        n = len(nums)
        curr_sum = 0
        for i in range(n):
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += nums[i]
            res = max(res, curr_sum)
        return res
        # Time = O(n)
        # Space = O(1)

def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solution_obj = Solution()
    res = solution_obj.get_max_subarray_sum(nums)
    print(f"Max Subarray sum in nums: {res}")


if __name__ == '__main__':
    main()
