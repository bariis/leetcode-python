"""
1. Two Sum
@Level: Easy

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""


class Solution:
    def twoSum(self, nums, target):
        if nums is None:
            return []

        to_search = dict()
        for idx, num in enumerate(nums):
            search = target - num
            if num not in to_search:
                to_search[search] = idx
            else:
                res = [to_search[num], idx]
                return res
        return []