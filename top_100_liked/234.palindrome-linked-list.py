# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        
        dummy = ListNode(None)
        dummy.next = head
        
        pre = None
        slow, fast = dummy, dummy
        
        while fast and fast.next:
            tmp = slow

            slow, fast = slow.next, fast.next.next
            
            # pre represents the last reversed node(the head of the reversed list)
            tmp.next = pre
            pre = tmp
        
        tmp = slow.next
        # 奇数链表
        if not fast:
            slow = pre
        # 偶数链表
        else:
            slow.next = pre
        fast = tmp
        
        while slow and fast:
            if slow.val != fast.val:
                return False
            slow, fast = slow.next, fast.next
        return True