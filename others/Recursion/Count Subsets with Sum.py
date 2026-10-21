# https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1

class Solution:
    def get_subsets(self, arr, target, start, curr_sum):
        if start == len(arr):
            if curr_sum == target:
                return 1
            return 0
        if curr_sum > target:
            return 0
        return self.get_subsets(arr, target, start+1, curr_sum+arr[start]) + self.get_subsets(arr, target, start+1, curr_sum)

    def perfectSum(self, arr, target):
		# code here
        return self.get_subsets(arr, target, 0, 0)
		
		# Time Complexity: O(2**n)
		# Space Complexity: O(n)