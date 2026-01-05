# #1 - Two Sum
# Problem solved by Adity
# Time Complexity: O(n) - We iterate through the list once, and dictionary lookups are O(1)
# Space Complexity: O(n) - We use extra space for the indexarr dictionary


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexarr = {}

        # Iterate through the list to find the complement
        for index, n in enumerate(nums):
            complement = target - n

            # If complement is already in the dictionary, return the indices
            if complement in indexarr:
                return (indexarr[complement], index)

            # Store the current number and its index
            indexarr[n] = index
