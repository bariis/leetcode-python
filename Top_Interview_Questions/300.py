"""
300. Longest Increasing Subsequence
@Level: Medium

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""

class Solution:
    def lengthOfLIS(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            memo = [0] * (len(nums))
            memo[0] = 1
            maxans = 1
            for i in range(len(memo)):
                maxval = 0
                for j in range(i):
                    if nums[i] > nums[j]:
                        maxval = max(maxval, memo[j])
                memo[i] = maxval + 1
                maxans = max(maxans, memo[i])
            return maxans