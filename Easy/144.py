# #144 - Binary Tree Preorder Traversal
# Problem solved by Adity
# Time Complexity: O(n) - each node is visited once
# Space Complexity: O(h) - recursion stack, where h is the height of the tree

from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if node is None:
                return

            result.append(node.val)   # Root
            dfs(node.left)            # Left
            dfs(node.right)           # Right

        dfs(root)
        return result
