# #35 - Search Insert Position
# Problem solved by Adity
# Time Complexity: O(log n) - binary search on sorted array
# Space Complexity: O(1) - constant extra space


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = len(nums) - 1
        j = 0

        while j <= l:
            m = (j + l) // 2
            if nums[m] == target:
                return m
            elif target > nums[m]:
                j = m + 1
            else:
                l = m - 1
        return j
