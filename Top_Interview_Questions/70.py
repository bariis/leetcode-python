"""
70. Climbing Stairs
@Level: Easy

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""

# Iterative Solution
class Solution:
    def climbStairs(self, n):
        if n < 1:
            return 0
        elif n == 1:
            return 1
        else:
            memo = [0] * (n+1)
            memo[1] = 1
            memo[2] = 2
            for i in range(3, n+1):
                memo[i] = memo[i-1] + memo[i-2]
            return memo[-1]


# Recursive Solution
class Solution_Recursive:
    def climbStairs(self, n: int) -> int:
        def climb_stairs(i):
            if i > n:
                return 0
            elif i == n:
                return 1
            elif memo[i] > 0:
                return memo[i]
            else:
                memo[i] = climb_stairs(i+1) + climb_stairs(i+2)
                return memo[i]
            
        memo = [0] * (n+1)
        climb_stairs(0)
        return memo[0]