# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def _rob(node):
            if not node:
                return 0, 0
            l_max, l_son_max = _rob(node.left)
            r_max, r_son_max = _rob(node.right)
            
            # left: incuding node; right: excuding node
            return max(node.val+l_son_max+r_son_max, l_max+r_max), l_max+r_max
        
        return _rob(root)[0]