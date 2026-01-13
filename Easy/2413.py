# #2413 - Smallest Even Multiple
# Problem solved by Adity
# Time Complexity: O(1) - Constant time check
# Space Complexity: O(1) - No extra space used


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return lcm(n,2)


        # If n is even, it is already the smallest even multiple
        #if n % 2 == 0:
         #   return n

        # If n is odd, multiply by 2 to get the smallest even multiple
        #return 2 * n
