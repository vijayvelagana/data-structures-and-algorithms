class Solution:
    def get_subsets(self, nums, start, end, res, temp):
        if start > end:
            res.append(temp.copy())
            return
        temp.append(nums[start])
        self.get_subsets(nums, start+1, end, res, temp)
        temp.pop()
        self.get_subsets(nums, start+1, end, res, temp)

    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        temp = []
        n = len(nums)
        self.get_subsets(nums, 0, n-1, res, temp)
        return res

# https://leetcode.com/problems/subsets/