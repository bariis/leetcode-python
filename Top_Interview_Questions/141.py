"""
141. Linked List Cycle
@Level: Easy

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Hash Table Approach
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodeList = set()
        
        while ((head is not None) and (head not in nodeList)):
            nodeList.add(head)
            head = head.next
        if(head is None):
            return False
        else:
            return True


# 2 Pointer Approach
class Solution_2:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False