"""
118. Pascal's Triangle
@Level: Easy

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
"""

class Solution:
    def generate(self, numRows):
        result = []
        prev = [1]
        for i in range(numRows):
            if i == 0:
                result.append(prev)
            else:
                current = [1] * (len(prev) + 1)
                for i in range(len(prev)-1):
                    current[i+1] = prev[i] + prev[i+1] 
                result.append(current)
                prev = current
        return result