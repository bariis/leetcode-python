"""
234. Palindrome Linked List
@Level: Easy

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # locate the middle of a linkedlist
        # 1. I can keep the linkedlist items in a list
        # 2. I can reverse the linkedlist as I iterate then use the list to check palindromes
        size = 0
        iterPtr = head
        l = []
        while iterPtr is not None:
            size += 1
            l.append(iterPtr.val)
            iterPtr = iterPtr.next
        
        for i in range(int(size//2)):
            if l[size-i-1] != l[i]:
                return False
            
        return True