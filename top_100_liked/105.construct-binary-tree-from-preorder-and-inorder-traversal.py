# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder.pop(0))
        
        root.left = self.buildTree(preorder[:root_index], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index:], inorder[root_index + 1:])
        return root