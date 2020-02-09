# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        start = ListNode(0)
        start.next = head
        
        curr = head.next
        while curr:
            next_node = curr.next
            
            head.next = next_node
            curr.next = start.next
            start.next = curr
            
            curr = next_node
            
        return start.next