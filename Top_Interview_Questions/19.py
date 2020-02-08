"""
19. Remove Nth Node From End of List
@Level: Medium

Given a linked list, remove the n-th node from the end of list and return its head.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        # n determines the number of .next.next we are going to call
        cur = head
        if(cur == None):
            return False
        arr = []
        while(cur != None):
            arr.append(cur.val)
            cur = cur.next
        arr.pop(len(arr)-n)
        return arr
    

# One pass solution space optimized
class Solution_opt:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        # n determines the number of .next.next we are going to call
        start = ListNode(0)
        slow, fast = start, start
        slow.next = head



        for _ in range(n+1):
            fast = fast.next
        
        while fast is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return start.next

