# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        def traverse(t1, t2):
            t2.val += t1.val
            if t1.left and t2.left:
                traverse(t1.left, t2.left)
            elif t1.left:
                t2.left = t1.left
            
            if t1.right and t2.right:
                traverse(t1.right, t2.right)
            elif t1.right:
                t2.right = t1.right
        
        if t1 and t2:
            traverse(t1, t2)
            return t2
        else:
            return t1 or t2
