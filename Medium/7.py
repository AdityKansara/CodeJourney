# #7 - Reverse Integer
# Problem solved by Adity
# Time Complexity: O(log10(n)) - We process each digit once.
# Space Complexity: O(1) - No extra space used apart from variables.

class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        y = abs(x)
        sign = 1 if x >= 0 else -1
        
        while y > 0:
            lastDigit = y % 10
            ans = lastDigit + ans * 10
            y = y // 10
        
        if ans >= pow(2, 31) - 1 or ans <= -pow(2, 31) - 1:
            return 0
        
        return sign * ans