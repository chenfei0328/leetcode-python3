# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxSum = root.val
        
        def traverse(node):
            nonlocal maxSum 
            val = node.val
            leftSum, rightSum = float('-inf'), float('-inf')
            if node.left:
                leftSum = traverse(node.left)
            if node.right:
                rightSum = traverse(node.right)
            maxVal = max(val, val + leftSum + rightSum, val + leftSum, val + rightSum)
            maxSum = max(maxSum, maxVal)
            return max(val, val + leftSum, val + rightSum)
                
        traverse(root)
        return maxSum