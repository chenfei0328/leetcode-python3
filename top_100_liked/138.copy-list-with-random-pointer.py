"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        curr = head
        hashmap = {} 
        
        while curr:
            if curr not in hashmap:
                hashmap[curr] = Node(curr.val, None, None)
            if curr.next:
                if curr.next not in hashmap:
                    hashmap[curr.next] = Node(curr.next.val, None, None)
                hashmap[curr].next = hashmap[curr.next]
            if curr.random:
                if curr.random not in hashmap:
                    hashmap[curr.random] = Node(curr.random.val, None, None)
                hashmap[curr].random = hashmap[curr.random]
            curr = curr.next
        
        return hashmap[head]