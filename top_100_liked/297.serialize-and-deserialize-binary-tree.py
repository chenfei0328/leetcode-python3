# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = [root]
        result = []
        
        while q:
            node = q.pop(0)
            if node:
                result.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                result.append(None)
                
        while len(result) > 1 and result[-1] == None:
            result.pop()
        
        return str(result)                  

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.strip('[[]]')
        data = data.split(',')

        data = [int(item) if item[-1] >= '0' and item[-1] <= '9' else None for item in data]

        if data:
            root = TreeNode(data[0])
            data.pop(0)
        else:
            return None
        
        q = [root]
        while q:
            node = q.pop(0)
            if data:
                node.left = TreeNode(data.pop(0))
                q.append(node.left)
            if data:
                node.right = TreeNode(data.pop(0))
                q.append(node.right)
        
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))








from queue import deque
class Codec:
    def __init__(self):
        pass
    def serialize(self, root):
        if root is None:
            return ''
        data = ''
        def dfs(root):
            nonlocal data
            if root:
                data += str(root.val) + ","
                dfs(root.left)
                dfs(root.right)
            else:
                data += 'x,'
        dfs(root)
        return data.rstrip(',')
        
    def deserialize(self, data):
        if data == '':
            return []
        data = deque(data.split(','))
        def helper(data):
            val = data.popleft()
            if val == 'x':
                return None
            else:
                node = TreeNode(val)
                node.left = helper(data)
                node.right = helper(data)
                return node
        return helper(data)