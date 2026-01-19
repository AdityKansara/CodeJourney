# LeetCode 258 - Add Digits
# Problem solved by Adity
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            s = 0
            while num > 0:
                s += num % 10
                num //= 10
            num = s
        return num


# LeetCode 258 - Add Digits
# Best solution (Digital Root)
# Time Complexity: O(1)
# Space Complexity: O(1)

# class Solution:
#     def addDigits(self, num: int) -> int:
#         if num == 0:
#             return 0
#         return 1 + (num - 1) % 9
