# #50 - Pow(x, n)
# Problem solved by Adity
# Time Complexity: O(log n) - Exponent is reduced by half each iteration.
# Space Complexity: O(1) - No extra space used apart from variables.

class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        
        if n < 0:
            x = 1 / x
            n = -n
        
        while n > 0:
            if n % 2 != 0:
                ans = ans * x
                n = n - 1
            x = x * x
            n = n // 2
        
        return ans