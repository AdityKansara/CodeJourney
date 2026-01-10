# #66 - Plus One
# Problem solved by Adity
# Time Complexity: O(n) - single pass through the digits
# Space Complexity: O(n) - output array

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        a = []

        for i, val in enumerate(digits[::-1]):
            if i == 0:
                ans = val + carry + 1
            else:
                ans = val + carry

            carry = 0

            if ans < 10:
                a.append(ans)
            else:
                a.append(ans % 10)
                carry = 1

        if carry == 1:
            a.append(1)

        return a[::-1]
