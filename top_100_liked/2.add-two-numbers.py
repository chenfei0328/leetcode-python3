# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head, l3 = None, None
        carry = 0
        
        while l1 or l2 or carry > 0:
            tempSum = 0
            
            if carry:
                tempSum += carry
            if l1:
                tempSum += l1.val
                l1 = l1.next
            if l2:
                tempSum += l2.val
                l2 = l2.next
            
            carry = tempSum // 10
            value = tempSum % 10
            
            if l3 == None:
                l3 = ListNode(value)
                head = l3
            else:
                l3.next = ListNode(value)
                l3 = l3.next
        
        return head
                
        