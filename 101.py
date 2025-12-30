# Problem 101 - Symmetric Tree
# Problem solved by Adity
# Time Complexity: O(n)  - Each node is visited once.
# Space Complexity: O(h) - Recursion stack where h is the height of the tree.

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Checks whether a binary tree is symmetric around its center.
        """

        def isMirror(leftNode: Optional[TreeNode], rightNode: Optional[TreeNode]) -> bool:
            """
            Recursively compares two nodes in mirror positions.
            """

            # If both nodes are None, symmetry is preserved
            if not leftNode and not rightNode:
                return True

            # If only one node exists, symmetry breaks
            if not leftNode or not rightNode:
                return False

            # If values differ, symmetry breaks
            if leftNode.val != rightNode.val:
                return False

            # Compare outer and inner mirrored children
            return (
                isMirror(leftNode.left, rightNode.right) and
                isMirror(leftNode.right, rightNode.left)
            )

        # Start comparison from the root’s left and right children
        return isMirror(root.left, root.right)
