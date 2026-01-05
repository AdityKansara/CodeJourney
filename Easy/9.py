# #9 - Palindrome Number
# Problem solved by Adity
# Time Complexity: O(log(x)) - The number of digits in x determines the loop iterations.
# Space Complexity: O(1) - Constant space used, no extra data structures.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Check if the number is negative, as negative numbers can't be palindromes
        if x < 0:
            return False

        r = 0  # Reverse of the number
        t = x  # Store the original number

        # Reverse the digits of the number
        while x != 0:
            r = r * 10 + int(x % 10)
            x = int(x / 10)

        # Check if the reversed number is equal to the original number
        if r == t:
            return True
        else:
            return False
