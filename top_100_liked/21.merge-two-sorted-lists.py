# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not (l1 or l2):
            return None
        head = l = ListNode(0)
        head.next = l

        while l1 and l2:
            if l1.val < l2.val:
                l.next = ListNode(l1.val) 
                l1 = l1.next
            else:
                l.next = ListNode(l2.val)
                l2 = l2.next
            l = l.next
        if l1:
            l.next = l1
        else:
            l.next = l2
        
        return head.next