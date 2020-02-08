"""
124. Binary Tree Maximum Path Sum
@Level: Hard

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if node is None:
                return 0
            left_sum = max(0, dfs(node.left))
            right_sum = max(0, dfs(node.right))
            
            self.max_sum = max(self.max_sum, left_sum + right_sum + node.val)
            
            return max(left_sum, right_sum) + node.val
        
        if root is None:
            return 0
        
        self.max_sum = float('-inf')
        dfs(root)
        return self.max_sum