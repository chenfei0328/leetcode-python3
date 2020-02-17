# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # root = TreeNode(None)
        def createNode(array):
            l = len(array)
            if l > 0:
                index = l // 2
                val = array[index]
                node = TreeNode(val)
                node.left = createNode(array[0:index])
                node.right = createNode(array[index+1:])
                return node
            else:
                return None
        
        root = createNode(nums)
        return root