# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum=0
        def fun(root):
            if root:
                if root.left:
                    if root.left.left==None and root.left.right==None:
                        self.sum=self.sum+root.left.val
                fun(root.left)
                fun(root.right)
            else:
                return
        fun(root)
        return self.sum