# #242 - Valid Anagram
# Problem solved by Adity
# Time Complexity: O(n)
# Space Complexity: O(1)

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = Counter(s)
        y = Counter(t)
        return x == y
