"""
215. Kth Largest Element in an Array
@Level: Medium

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

class Solution:
    def minHeapDelete(self, heap):
        min_idx, min_item = 0, heap[0]
        for i in range(1, len(heap)):
            if heap[i] < min_item:
                min_idx, min_item = i, heap[i]
        del heap[min_idx]
        return min_item
        
        
    def findKthLargest(self, nums, k):
        min_heap = []
        for num in nums:
            min_heap.append(num)
            if len(min_heap) > k:
                _ = self.minHeapDelete(min_heap)
        return self.minHeapDelete(min_heap)


class Solution_2:
    def findKthLargest(self, nums, k):
        nums = sorted(nums, reverse = True)
        for idx in range(len(nums)):
            if idx+1 == k:
                return nums[idx]
        return 0