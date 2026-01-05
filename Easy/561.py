# #561 - Array Partition
# Problem solved by Adity
# Time Complexity: O(n log n) - Sorting the array takes O(n log n)
# Space Complexity: O(1) - No extra space used other than input storage


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Sort the input list to ensure that pairs of numbers are in increasing order
        nums.sort()

        # Initialize max to 0 to keep track of the sum of the minimums of pairs
        max = 0

        # Loop through the sorted list, stepping by 2 to handle pairs
        for i in range(len(nums)):
            # Skip the second number in each pair (index 1, 3, 5, ...) as we are only interested in the first number
            if i % 2 != 0:
                continue

            # Add the minimum of the current pair (nums[i], nums[i + 1]) to max
            max = max + min(nums[i], nums[i + 1])

        # Return the final sum of the minimums of all pairs
        return max
