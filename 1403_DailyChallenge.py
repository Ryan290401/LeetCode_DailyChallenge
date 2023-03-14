# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def solve(root, val):
            if not root:
                return 0

            if not root.left and not root.right:
                res = val*10 + root.val
                return res

            res = val*10 + root.val
            return solve(root.left, res) + solve(root.right, res)

        return solve(root, 0)