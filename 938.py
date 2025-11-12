# Problem 938 - Range Sum of BST
# Problem solved by Adity
# Time Complexity: O(n) - Visits only relevant nodes
# Space Complexity: O(h) - Due to recursion stack (h = tree height)

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        # If the current node is too small, skip left
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        
        # If the current node is too large, skip right
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        
        # Current node is in range — include it
        return (
            root.val +
            self.rangeSumBST(root.left, low, high) +
            self.rangeSumBST(root.right, low, high)
        )
