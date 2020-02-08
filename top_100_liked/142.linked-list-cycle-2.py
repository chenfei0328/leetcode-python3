# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        node_set = []
        while head:
            if head not in node_set:
                node_set.append(head)
            else:
                return head
            head = head.next
            
        return None