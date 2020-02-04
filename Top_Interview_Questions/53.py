"""
53. Maximum Subarray
@Level: Easy

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        dp = [float('-inf')] * len(nums)
        dp[0] = nums[0]
            
  
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
 
        return max(dp)