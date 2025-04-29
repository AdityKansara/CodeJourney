# #2357 - Make Array Zero by Subtracting Equal Amounts
# Problem solved by Adity
# Time Complexity: O(n^2) - Two nested loops (one for finding the smallest element and another for reducing elements)
# Space Complexity: O(1) - Constant space used, no additional data structures

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        s = 0
        
        # If all elements are 0, no operations are needed
        if all(num == 0 for num in nums):
            return 0

        # Loop until all elements become zero
        for j in range(len(nums)):
            smallest = 101  # Initialize smallest to a value larger than any element in nums
            
            # Find the smallest positive number in the array
            for i in range(len(nums)):
                if nums[i] > 0 and nums[i] < smallest:
                    smallest = nums[i]

            # Subtract the smallest positive number from all elements
            for i in range(len(nums)):
                if nums[i] > 0:
                    nums[i] = nums[i] - smallest
            
            # Count how many elements have become zero
            s = 0
            for i in range(len(nums)):
                if nums[i] == 0:
                    s = s + 1
            
            count = count + 1  # Increase the operation count

            # If all elements are zero, break the loop
            if s == len(nums):
                break

        return count
