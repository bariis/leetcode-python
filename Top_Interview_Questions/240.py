"""
240. Search a 2D Matrix II
@Level: Medium

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

* Integers in each row are sorted in ascending from left to right.
* Integers in each column are sorted in ascending from top to bottom.
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix) < 1 or len(matrix[0]) < 1:
            return False
        if matrix:
            row,col,width=len(matrix)-1,0,len(matrix[0])
            while row>=0 and col<width:
                if matrix[row][col]==target:
                    return True
                elif matrix[row][col]>target:
                    row=row-1
                else:
                    col=col+1
            return False