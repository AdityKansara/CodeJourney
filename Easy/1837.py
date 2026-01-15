# #1837 - Sum of Digits in Base K
# Problem solved by Adity
# Time Complexity: O(logₖ n)
# Space Complexity: O(1)


class Solution:
    def sumBase(self, n: int, k: int) -> int:
        a = []
        while n >= k:
            a.append(n % k)
            n //= k
        a.append(n)
        return sum(a)
