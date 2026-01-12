# #283 - Move Zeroes
# Problem solved by Adity
# Time Complexity: O(n) - single pass through the array
# Space Complexity: O(1) - in-place modification


# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         j = 0
#         # l = len(nums)
#         for i,val in enumerate(nums):
#             while val != 0:
#                 nums[j] = val
#                 val = 0
#                 j = j + 1
#             if i == len(nums)-1:
#                 for _ in range(j,len(nums)):
#                     nums[j] = 0
#                     j = j + 1
            
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0  # next position for non-zero

        # Move all non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        # Fill the remaining positions with zeroes
        for k in range(j, len(nums)):
            nums[k] = 0

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         j = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[j], nums[i] = nums[i], nums[j]
#                 j += 1
