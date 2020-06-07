"""
1007. Minimum Domino Rotations For Equal Row
@Level: Medium

In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.
"""

class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        a_cnt, b_cnt = 0, 0
        for i in range(n):
            if A[i] != A[0] and B[i] != A[0]:
                break
            if A[i] != A[0]:
                a_cnt += 1;
            if B[i] != A[0]:
                b_cnt += 1;
            if i == (n-1):
                return min(a_cnt, b_cnt)
        a_cnt, b_cnt = 0, 0
        for i in range(n):
            if A[i] != B[0] and B[i] != B[0]:
                return -1
            if A[i] != B[0]:
                a_cnt += 1;
            if B[i] != B[0]:
                b_cnt += 1;
            if i == (n-1):
                return min(a_cnt, b_cnt)
        return -1