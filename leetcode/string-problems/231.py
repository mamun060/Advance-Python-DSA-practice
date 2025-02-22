# Leetcode-231: Power of Two problem
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while n % 2 == 0:
            n = n / 2
        if n == 1:
            return True
            
Solution = Solution()
print(Solution.isPowerOfTwo(16))