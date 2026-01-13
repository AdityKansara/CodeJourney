# #1342 - Number of Steps to Reduce a Number to Zero
# Problem solved by Adity
# Time Complexity: O(log n) - Each step reduces the number significantly
# Space Complexity: O(1) - No extra space used


class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0

        # Continue until num becomes zero
        while num != 0:
            # If num is even, divide by 2
            if num % 2 == 0:
                num //= 2
            else:
                # If num is odd, subtract 1
                num -= 1

            steps += 1

        return steps
