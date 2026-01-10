# #268 - Missing Number
# Problem solved by Adity
# Time Complexity: O(n) - single pass through the array
# Space Complexity: O(1) - constant extra space

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = 0
        n = len(nums)

        for i in nums:
            s = s + i

        nSum = (n * (n + 1)) // 2

        return nSum - s


# O(n) time
# O(1) extra space
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         ans = len(nums)

#         for i, val in enumerate(nums):
#             ans ^= i
#             ans ^= val

#         return ans
