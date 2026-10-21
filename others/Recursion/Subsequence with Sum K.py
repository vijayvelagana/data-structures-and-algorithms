class Solution:
    def get_subsets(self, arr, k, start, curr_sum):
        if curr_sum == k:
            return True
        if start == len(arr) or curr_sum > k:
            return False
        return self.get_subsets(arr, k, start+1, curr_sum+arr[start]) or self.get_subsets(arr, k, start+1, curr_sum)
    
    def checkSubsequenceSum(self, arr, k):
        # code here
        return self.get_subsets(arr, k, 0, 0)
        
        # Time Complexity: O(2**n)
        # Space Complexity: O(n), recursion stack space
        # https://www.geeksforgeeks.org/problems/check-if-there-exists-a-subsequence-with-sum-k/1
        