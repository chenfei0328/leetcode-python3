# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA, curB = headA, headB
        
        lenA, lenB = 0, 0
        while curA:
            curA = curA.next
            lenA += 1
        while curB:
            curB = curB.next
            lenB += 1
        
        curA, curB = headA, headB
        if lenA < lenB:
            i = 0
            while i < lenB - lenA:
                curB = curB.next
                i += 1
            while curA and curB:
                if curA == curB:
                    return curA
                else:
                    curA = curA.next
                    curB = curB.next
            return None
        else:
            i = 0
            while i < lenA - lenB:
                curA = curA.next
                i += 1
            while curA and curB:
                if curA == curB:
                    return curA
                else:
                    curA = curA.next
                    curB = curB.next
            return None



class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:     
        d = {}
        while headA:
            d[headA] = 1
            headA = headA.next
    
        while headB:
            if headB in d:
                return headB
            headB = headB.next
        return None