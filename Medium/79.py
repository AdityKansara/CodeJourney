# LeetCode 79 - Word Search
# Problem solved by Adity
# Time Complexity: O(N * M * 4^L)
#   - N * M = total cells
#   - L = length of word (each DFS explores up to 4 neighbors per step)
# Space Complexity: O(L)
#   - recursion stack depth proportional to the length of the word

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r: int, c: int, i: int) -> bool:
            # All characters matched
            if i == len(word):
                return True

            # Out of bounds or mismatch
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False

            # Mark as visited
            temp = board[r][c]
            board[r][c] = "#"

            # Explore neighbors
            found = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )

            # Restore original value
            board[r][c] = temp
            return found

        # Try starting DFS from each cell
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False
