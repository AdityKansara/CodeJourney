# #104 - Maximum Depth of Binary Tree
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if node is None:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            return 1 + max(left_depth, right_depth)

        return dfs(root)
