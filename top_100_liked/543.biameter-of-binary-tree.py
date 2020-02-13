# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_len = 0
        
        def traverse(node):
            nonlocal max_len
            if node:
                left_len = traverse(node.left)
                right_len = traverse(node.right)
                
                max_len = max(max_len, left_len + right_len)
                return max(left_len, right_len) + 1
            else:
                return 0
            
        traverse(root)
        return max_len