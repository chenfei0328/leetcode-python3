# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        val = []
        while head:
            val.append(head.val)
            head = head.next
        
        if not val:
            return None
        else:
            val.sort()
            curr = ListNode(0)
            head = curr
            for num in val:
                curr.next = ListNode(num)
                curr = curr.next
            return head.next
        