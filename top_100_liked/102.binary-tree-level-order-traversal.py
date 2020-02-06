# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = [[root, 0]]
        ans = []
        while q:
            item = q.pop(0)
            node = item[0]
            level = item[1]
            
            if node:
                if len(ans) == level:
                    ans.append([])
                ans[level].append(node.val)
                q.append([node.left, level + 1])
                q.append([node.right, level + 1])
            
        return ans