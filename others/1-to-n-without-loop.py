class Solution:
    def printTillN(self, n):
    	#code here 
    	if n <= 0:
    	    return 
    	self.printTillN(n-1)
    	print(n, end=" ")
    	# Time complexity = O(n)
    	# Space complexity = O(n) = Recursion stack
    	
solution_obj = Solution()
solution_obj.printTillN(10)
