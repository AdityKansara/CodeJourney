# #2769 - Find the Distance Value Between Mirror Numbers
# Problem solved by Adity
# Time Complexity: O(d)
# Space Complexity: O(d)


class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev = str(n)[::-1]
        return abs(int(rev) - n)
