"""
33. Search in Rotated Sorted Array
Level: Medium
 
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
"""


class Solution:
    def search(self, nums, target):
        if nums is None or len(nums) == 0:
            return -1
        start, end = 0, len(nums)-1
        while start < end:
            mid = (start+end)//2
            if nums[mid] > nums[end]:
                if target > nums[mid] or target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid
            else:
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid
        if start == end and target != nums[start]:
            return -1
        else:
            return start

            