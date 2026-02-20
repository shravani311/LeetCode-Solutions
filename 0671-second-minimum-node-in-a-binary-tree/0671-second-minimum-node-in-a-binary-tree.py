# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        l=[]
        def fun(root):
            if root:
                l.append(root.val)
                fun(root.left)
                fun(root.right)
            else:
                return
        fun(root)
        l=set(l)
        l=list(l)
        l.sort()
        if len(l)>1:
                return l[1]
        else:
                return -1
