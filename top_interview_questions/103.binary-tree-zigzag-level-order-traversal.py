# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        left = [root]
        right = []
        output = []
        
        while left or right:
            tmp = []
            while left:
                node = left.pop()
                if node:
                    tmp.append(node.val)
                    right.append(node.left)
                    right.append(node.right)
            
            if tmp:
                output.append(tmp[:])
                tmp = []
            else:
                return output
            
            while right:
                node = right.pop()
                if node:
                    tmp.append(node.val)
                    left.append(node.right)
                    left.append(node.left)
                
            if tmp:
                output.append(tmp[:])
            else:
                return output
            
        # return output
                