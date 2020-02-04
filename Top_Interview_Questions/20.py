"""
20. Valid Parentheses
@Level: Easy

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
       
        stack = []
        stackPairs = {"(":")", "{":"}", "[":"]"}
        
        for e in s:
            if(e == "(" or e == "{" or e == "["):
                stack.append(e)
            else:
                if(len(stack) != 0):
                    current = stack.pop()
                    if(stackPairs[current] != e):
                        return False
                else:
                    return False
        if(len(stack) == 0):
            return True
        else:
            return False
        