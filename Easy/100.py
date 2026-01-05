# LeetCode 100 - Same Tree
# Problem solved by Adity
# Time Complexity: O(N) - visits each node once, N = number of nodes in tree
# Space Complexity: O(N) - recursion stack + node list storage

from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(current: Optional[TreeNode]) -> List:
            nodelist = []

            def dfs(node: Optional[TreeNode]):
                if node is None:
                    nodelist.append("null")
                    return

                nodelist.append(node.val)
                dfs(node.left)
                dfs(node.right)

            dfs(current)
            return nodelist

        pNodes = traverse(p)
        qNodes = traverse(q)

        return pNodes == qNodes
