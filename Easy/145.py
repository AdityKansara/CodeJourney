# #145 - Binary Tree Postorder Traversal
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if node is None:
                return

            dfs(node.left)    # Left
            dfs(node.right)   # Right
            result.append(node.val)  # Root

        dfs(root)
        return result
