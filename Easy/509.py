# #509 - Fibonacci Number
# Problem solved by Adity
# Approach: Recursion
# Time Complexity: O(2^n) - exponential due to repeated subproblems
# Space Complexity: O(n) - recursion stack


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        return self.fib(n - 1) + self.fib(n - 2)


# Approach: Iterative
# Time Complexity: O(n) - single pass
# Space Complexity: O(1) - constant extra space

# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1

#         a, b = 0, 1

#         for _ in range(2, n + 1):
#             a, b = b, a + b

#         return b
