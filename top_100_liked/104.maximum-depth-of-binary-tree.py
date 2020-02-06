# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        maxD = 0
        
        def preOrder(node, level):
            if node:
                level += 1
                nonlocal maxD
                maxD = max(maxD, level)
                preOrder(node.left, level)
                preOrder(node.right, level)
                
        preOrder(root, 0)
        return maxD