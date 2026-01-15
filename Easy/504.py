# #504 - Base 7
# Problem solved by Adity
# Time Complexity: O(log₇ n)
# Space Complexity: O(1)


class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = ""
        a = num
        num = abs(num)

        while num >= 7:
            ans += str(num % 7)
            num //= 7
        ans += str(num)

        if a < 0:
            ans += "-"
        return ans[::-1]
