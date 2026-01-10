# #367 - Valid Perfect Square
# Problem solved by Adity
# Time Complexity: O(log n) - binary search on the answer
# Space Complexity: O(1) - constant extra space


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num

        while l <= r:
            mid = (l + r) // 2
            sq = mid * mid

            if sq == num:
                return True
            elif sq > num:
                r = mid - 1
            else:
                l = mid + 1

        return False
