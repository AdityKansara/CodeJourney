# #3512 - Minimum Operations to Make Array Elements Divisible by K
# Problem solved by Adity
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k
