# LeetCode 94 - Binary Tree Inorder Traversal
# Problem solved by Adity
# Time Complexity: O(N) - visits each node exactly once
# Space Complexity: O(H) - recursion stack, H = height of tree

from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []

        def traverse(rt: Optional[TreeNode]):
            if rt is None:
                return
            if rt.left is not None:
                traverse(rt.left)
            nodes.append(rt.val)
            if rt.right is not None:
                traverse(rt.right)

        traverse(root)
        return nodes
