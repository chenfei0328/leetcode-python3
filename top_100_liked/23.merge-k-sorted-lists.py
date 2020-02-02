# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = p = ListNode(0)
        q = PriorityQueue()
        
        for index, l in enumerate(lists):
            if l:
                q.put((l.val, index, l))
       
        while not q.empty():
            val, index, node = q.get()
            p.next = ListNode(val)
            p = p.next
            node = node.next
            if node:
                q.put((node.val, index, node))
        
        return head.next





from queue import PriorityQueue

# https://stackoverflow.com/questions/40205223/priority-queue-with-tuples-and-dicts
class use_only_first:
    def __init__(self, first, second):
        self._first, self._second = first, second

    def __lt__(self, other):
        return self._first < other._first

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put(use_only_first(l.val, l))
        head = point = ListNode(0)
        while not q.empty():    # PriorityQueue has no len()
            use_object = q.get()
            val = use_object._first
            node = use_object._second
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put(use_only_first(node.val, node))
        return head.next



class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        m = []
        for i in lists:
            while(i):
                m.append(i.val)
                i = i.next
        m = sorted(m)
        out = k = ListNode(0)
        for i in m:
            k.next = ListNode(i)
            k = k.next
        return out.next




class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next