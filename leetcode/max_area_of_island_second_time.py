from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        ans = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    ans = max(ans, self.DFS(grid, [i, j]))
        return ans
    
    def isValid(self, R, C, x, y):
        return x >= 0 and x < R and y >= 0 and y < C
    
    def DFS(self, grid, position):
        R = len(grid)
        C = len(grid[0])
        x, y = position
        grid[x][y] = 0
        direction = [[1,0],[0,1],[0,-1],[-1,0]]
        ans = 0
        for dir in direction:
            newX, newY = x + dir[0], y + dir[1]
            if self.isValid(R, C, newX, newY) and grid[newX][newY] == 1:
                ans += self.DFS(grid, [newX, newY])
        return ans + 1
