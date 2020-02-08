"""
42. Trapping Rain Water
@Level: Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1:
            return 0
        ans = 0
        left_max = [] 
        right_max = [0] * len(height) 
        
        left_max.append(height[0])
        for i in range(1, len(height)):
            left_max.append(max(height[i], left_max[i-1]))
            
        right_max[len(right_max) - 1] = height[len(right_max) - 1]
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])
        for i in range(1, len(height)-1):
            ans += min(left_max[i], right_max[i]) - height[i]
        return ans
    