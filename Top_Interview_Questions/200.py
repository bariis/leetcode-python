"""
200. Number of Islands
@Level: Medium

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

class Solution:
    def numIslands(self, grid):
        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]) or grid[r][c] == '0' or visited[r][c] == True:
                return
            
            visited[r][c] = True
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
           
        
        num_islands = 0
        if grid is None or len(grid) == 0:
            return 0
        visited = []
        for i in range(len(grid)):
            visited.append([False] * len(grid[i]))
        
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and visited[i][j] == False:
                    num_islands += 1
                    dfs(i, j)
        return num_islands