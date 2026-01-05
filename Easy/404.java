// #404 - Sum of Left Leaves
// Problem solved by Adity
// Time Complexity: O(n) - Each node in the tree is visited once.
// Space Complexity: O(h) - Where h is the height of the tree due to recursive stack.

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int sumOfLeftLeaves(TreeNode root) {
        // Base case: if the node is null, return 0
        if (root == null) {
            return 0;
        }

        int sum = 0;

        // Check if the left child is a leaf node
        if (root.left != null && root.left.left == null && root.left.right == null) {
            sum += root.left.val; // Add its value to the sum
        }

        // Recursively call for left and right subtrees
        sum += sumOfLeftLeaves(root.left);
        sum += sumOfLeftLeaves(root.right);

        return sum;
    }
}
