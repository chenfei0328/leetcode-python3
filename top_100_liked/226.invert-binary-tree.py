# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:   
        def invert(node):
            tmp = node.left
            node.left = node.right
            node.right = tmp
            if node.left:
                invert(node.left)
            if node.right:
                invert(node.right)
        
        if root:
            invert(root)
        
        return root