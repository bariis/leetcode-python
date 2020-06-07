"""
525. Contiguous Array
@Level: Medium

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map_memo = dict()
        map_memo[0] = -1
        max_len, count = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count += -1
            if count in map_memo:
                max_len = max(max_len, i - map_memo[count])
            else:
                map_memo[count] = i
        return max_len