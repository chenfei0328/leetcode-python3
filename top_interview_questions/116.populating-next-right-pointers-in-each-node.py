"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        stack = [[root, 0]]
        last, last_level = Node(None), 0
        while stack:
            now = stack.pop(0)
            node = now[0]
            level = now[1]
            if node:
                if level == last_level:
                    last.next = node

                last = node
                last_level = level
                stack.append([node.left, level + 1])
                stack.append([node.right, level + 1])
                
        return root