# #231 - Power of Two
# Problem solved by Adity
# Time Complexity: O(log n) - repeatedly dividing by 2
# Space Complexity: O(1) - constant extra space


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        while n > 0:
            if n == 1:
                return True
            if n % 2 == 0:
                n = n // 2
            else:
                return False

        return True

# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         return n > 0 and (n & (n - 1)) == 0