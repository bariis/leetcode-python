"""
226. Invert Binary Tree
@Level: Easy
 
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        if root is None: return None
        queue = []
        queue.append(root)
        while len(queue) > 0:
            current = queue.pop(0)
            temp = current.left
            current.left = current.right
            current.right = temp
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        return root