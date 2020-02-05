"""
160. Intersection of Two Linked Lists
@Level: Easy

Write a program to find the node at which the intersection of two singly linked lists begins.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        dict_A = set()
        while headA is not None:
            dict_A.add(headA)
            headA = headA.next
        while headB is not None:
            if headB in dict_A:
                return headB
            headB = headB.next
        return None
