# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def traverse(current: Optional[TreeNode]) -> bool:
            lnodelist = []
            rnodelist = []

            def ldfs(node: Optional[TreeNode]):
                if node is None:
                    lnodelist.append("null")
                    return

                ldfs(node.left)
                lnodelist.append(node.val)
                ldfs(node.right)

            def rdfs(node: Optional[TreeNode]):
                if node is None:
                    rnodelist.append("null")
                    return

                rdfs(node.right)
                rnodelist.append(node.val)
                rdfs(node.left)

            ldfs(current.left)
            rdfs(current.right)
            print(lnodelist)
            print(rnodelist)

            if lnodelist == rnodelist:
                return True
            else:
                return False

        return traverse(root)
