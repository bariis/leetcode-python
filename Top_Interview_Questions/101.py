"""
101. Symmetric Tree
@Level: Easy

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetricHelper(self, left, right):
        if left is None or right is None:
            if left is None and right is None:
                return True
            else:
                return False
        if left.val != right.val:
            return False
        return self.isSymmetricHelper(left.left, right.right) and self.isSymmetricHelper(left.right, right.left)
        
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isSymmetricHelper(root.left, root.right)