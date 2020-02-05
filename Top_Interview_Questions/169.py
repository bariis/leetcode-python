"""
169. Majority Element
@Level: Easy

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""

# Sorting Solution
class Solution:
    def majorityElement(self, nums) -> int:
        nums = sorted(nums)
        return nums[len(nums)//2]

# Hash-Map Solution
class Solution_2:
    def majorityElement(self, nums) -> int:
        cnt = dict()
        for num in nums:
            if(num not in cnt.keys()):
                cnt[num] = 1 
            else:
                cnt[num] += 1 
        r = 0
        res = -1
        for k, v in cnt.items():
            if(v > r):
                r = v
                res = k
        return res
