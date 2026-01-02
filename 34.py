# #34 - Find First and Last Position of Element in Sorted Array
# Problem solved by Adity
# Time Complexity: O(log n) - Two binary searches on a sorted array.
# Space Complexity: O(1) - Constant extra space used.

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binarySearch(find_first: bool) -> int:
            low = 0
            high = len(nums) - 1
            index = -1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    index = mid
                    if find_first:
                        high = mid - 1  # move left
                    else:
                        low = mid + 1  # move right

            return index

        first = binarySearch(find_first=True)
        last = binarySearch(find_first=False)

        return [first, last]
