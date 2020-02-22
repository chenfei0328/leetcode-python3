# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        odd, even = head, head.next     
        
        while even and even.next:
            tmp = odd.next
            odd.next = even.next
            even.next = even.next.next
            odd.next.next = tmp
            
            odd, even = odd.next, even.next
            
        return dummy.next
            