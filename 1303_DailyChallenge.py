# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def solve(self,root_a, root_b):
        if not root_a and not root_b:
            return True
        if not root_a or not root_b:
            return False
        if root_a.val != root_b.val:
            return False

        return self.slove(root_a.left, root_b.right) and self.slove(root_a.right, root_b.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.slove(root.left, root.right)