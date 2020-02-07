# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.flatten(root.left)
        self.flatten(root.right)
        
        # left is empty
        if not root.left:
            return None
        
        # insert left into right
        node = root.left
        while node.right != None:
            node = node.right
        node.right = root.right
        root.right = root.left
        root.left = None
