# #110 - Balanced Binary Tree
# Problem solved by Adity
# Time Complexity: O(n) - each node is visited once
# Space Complexity: O(h) - recursion stack, where h is the height of the tree

from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root == None:
            return True

        def dfs(root):
            # Returns [is_balanced, height]
            if root == None:
                return [True, 0]

            l = dfs(root.left)
            r = dfs(root.right)

            balanced = l[0] and r[0] and abs(l[1] - r[1]) <= 1

            return [balanced, 1 + max(l[1], r[1])]

        return dfs(root)[0]
