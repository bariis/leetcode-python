"""
3. Longest Substring Without Repeating Characters
@Level: Medium

Given a string, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        mySet = set()
        i, j, ans = 0, 0, 0
        while(i < n and j < n):
            # extend the range [i, j]
            if(s[j] not in mySet):
                mySet.add(s[j])
                j += 1
                ans = max(ans, j - i)
            else:
                if s[i] in mySet:
                    mySet.remove(s[i])
                    i += 1
        return ans