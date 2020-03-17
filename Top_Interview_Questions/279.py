"""
279. Perfect Squares
@Level: Medium

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""


class Solution:
    def numSquares(self, n: int) -> int:

        if n <= 0:
            return 0
        
        squares = [n] * (n+1)
        squares[0] = 0
        squares[1] = 1
        for i in range(1, n+1):
            for j in range(1, i):
                if j*j > i:
                    break
                squares[i] = min(squares[i], squares[i - j*j] + 1)
        return squares[-1]