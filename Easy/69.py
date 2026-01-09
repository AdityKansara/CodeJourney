# #69 - Sqrt(x)
# Problem solved by Adity
# Time Complexity: O(log x) - binary search on the answer
# Space Complexity: O(1) - constant extra space

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l, r = 1, x // 2

        while l <= r:
            m = (l + r) // 2

            if m * m <= x:
                l = m + 1
            else:
                r = m - 1

        return r
