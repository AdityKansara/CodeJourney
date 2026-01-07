# #389 - Find the Difference
# Problem solved by Adity
# Time Complexity: O(n) - counting characters in both strings
# Space Complexity: O(1) - fixed alphabet size (constant extra space)

from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        countS = Counter(s)
        countT = Counter(t)

        for c in countT:
            if c not in countS:
                return c

            if countS[c] < countT[c]:
                return c


# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         sumS = sumT = 0
#         for c in s:
#             sumS = sumS + ord(c)

#         for c in t:
#             sumT = sumT + ord(c)

#         return chr(sumT - sumS)

# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         res = 0
#         for c in s:
#             res = ord(c) ^ res

#         for c in t:
#             res = ord(c) ^ res

#         return chr(res)
