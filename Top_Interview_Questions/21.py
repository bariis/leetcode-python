"""
21. Merge Two Sorted Lists
@Level: Easy

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        iterL1 = l1
        iterL2 = l2

        head = ListNode(0)
        current = head
        
        while((iterL1 != None) and (iterL2 != None)):
            
            if(iterL1.val < iterL2.val):
                current.next = ListNode(iterL1.val)
                current = current.next
                iterL1 = iterL1.next
            else:
                current.next = ListNode(iterL2.val) 
                current = current.next
                iterL2 = iterL2.next
                
        # check which list is empty       
        if(iterL1 is None):
            current.next = iterL2
        else:
            current.next = iterL1
        
        return head.next