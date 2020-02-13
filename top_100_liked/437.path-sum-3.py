# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        
        def findPath(node, res):
            nonlocal num
            if node:
                val = node.val
                if val == res:
                    num += 1
                    findPath(node.left, 0)
                    findPath(node.right, 0)
                else:
                    findPath(node.left, res-val)
                    findPath(node.right, res-val)
        
        def traverse(node):
            if node:
                findPath(node, sum)
                traverse(node.left)
                traverse(node.right)
                
        num = 0
        traverse(root)
        return num
    
    
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        count = 0
        def bfs(node, stack):
            if not node:
                return
            nonlocal count
            
            val = node.val
            stack = [num + val for num in stack]
            stack.append(val)
            count += stack.count(sum)
            # print(stack)
            # print(count)
            
            bfs(node.left, stack)
            bfs(node.right, stack)
        bfs(root,[])
        return count