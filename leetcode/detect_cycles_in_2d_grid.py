from typing import List

class Solution:
  def containsCycle(self, grid: List[List[str]]) -> bool:
    R, C = len(grid), len(grid[0])
    DIRECTION = [[1,0],[0,1],[-1,0],[0,-1]]
    visited = [[False for _ in range(C)] for _ in range(R)]
    def valid(x, y):
      return x >= 0 and x < R and y >= 0 and y < C
    def DFS(grid, point, origin, val):
      curX, curY = point
      visited[curX][curY] = True
      for x, y in DIRECTION:
        newX = x + curX
        newY = y + curY
        if valid(newX, newY):
          if visited[newX][newY] and grid[newX][newY] == val and (newX != origin[0] and newY != origin[1]):
            return True
          if not visited[newX][newY] and grid[newX][newY] == val:
            if DFS(grid, [newX, newY], [curX, curY], val):
              return True
      return False
    for i in range(R):
      for j in range(C):
        if not visited[i][j]:
          if DFS(grid, [i, j], [-1,-1], grid[i][j]):
            return True
    return False
          
sol = Solution()
assert sol.containsCycle([["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]) == True
assert sol.containsCycle([["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]) == True
assert sol.containsCycle([["a","b","b"],["b","z","b"],["b","b","a"]]) == False
assert sol.containsCycle([["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","a"]]) == False
assert sol.containsCycle([
  ["c","a","d"],
  ["a","a","a"],
  ["a","a","d"],
  ["a","c","d"],
  ["a","b","c"]]) == True
