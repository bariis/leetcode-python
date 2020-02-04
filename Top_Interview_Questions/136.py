"""
136. Single Number
@Level: Easy

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

# Hash-Set Solution
class Solution:
    def singleNumber(self, nums):
        unique = set()
        for i in range(len(nums)):
            if nums[i] not in unique:
                unique.add(nums[i])
            else:
                unique.remove(nums[i])
        return unique.pop()

# Logical Operator Solution (faster)
class Solution_2:
    def singleNumber(self, nums):
        odd_one = 0
        for i in range(len(nums)):
            odd_one ^= nums[i]
        return odd_one