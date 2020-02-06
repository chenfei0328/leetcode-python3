# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def show(root):
            if root:
                show(root.left)
                ans.append(root.val)
                show(root.right)
        show(root)
        return ans



class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        temp = []
        
        node = root
        while node or temp:
            while node:
                temp.append(node)
                node = node.left
            node = temp.pop()
            ans.append(node.val)
            node = node.right
        
        return ans