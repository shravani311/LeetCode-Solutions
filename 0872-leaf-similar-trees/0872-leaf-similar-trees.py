# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l=[]
        def fun(root):
            if root.left==None and root.right==None:
                l.append(root.val)
                return
            if root.left==None:
                return fun(root.right)
            if root.right==None:
                return fun(root.left)
            if root:
                fun(root.left)
                fun(root.right)
        fun(root1)
        ans=[]
        ans=l
        l=[]
        fun(root2)
        return l==ans