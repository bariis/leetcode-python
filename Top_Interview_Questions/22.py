"""
22. Generate Parentheses
@Level: Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        chosen = []
        def generate(s = "", left = 0, right = 0):
            if(len(s) == 2 * n):
                chosen.append(s)
                return
            if left < n:
                generate(s + "(", left + 1, right)
            if right < left:
                generate(s + ")", left, right + 1)
        
        generate()
        return chosen


