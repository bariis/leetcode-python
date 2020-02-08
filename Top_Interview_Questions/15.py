"""
15. 3Sum
@Level: Medium

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) < 3:
            return []
        res = []
        balance = 0
        nums.sort()
        for i in range(len(nums)):
            if i != 0 and nums[i-1] == nums[i]: continue
            j = i + 1
            k = len(nums)-1
            while j < k:
                balance = nums[i] + nums[j] + nums[k]
                if balance == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]: j+=1
                elif balance > 0:
                    k -= 1
                else:
                    j += 1
        return res