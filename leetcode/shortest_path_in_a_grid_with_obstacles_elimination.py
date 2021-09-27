from typing import List

class Solution:
  def shortestPath(self, grid: List[List[int]], k: int) -> int:
    R = len(grid)
    C = len(grid[0])
    if R == 1 and C == 1:
      return 0
    if k >= R + C - 3:
      return R + C - 2
    direction = [[0, 1],[0,-1],[1,0],[-1,0]]
    visited = set([(0,0,k)])
    def isNotValid(x, y):
      return x < 0 or y < 0 or x >= R or y >= C
    def bfs(grid):
      queue = [(0,0,k,0)]
      while len(queue) > 0:
        size = len(queue)
        for _ in range(size):
          x, y, eliminate, step = queue.pop(0)
          for i in range(4):
            newX = x + direction[i][0]
            newY = y + direction[i][1]
            if isNotValid(newX, newY):
              continue
            if grid[newX][newY] == 1 and eliminate > 0 and (newX, newY, eliminate - 1) not in visited:
              visited.add((newX, newY, eliminate - 1))
              queue.append((newX, newY, eliminate - 1, step + 1))
            if grid[newX][newY] == 0 and (newX, newY, eliminate) not in visited:
              if newX == R - 1 and newY == C - 1:
                return step + 1
              visited.add((newX, newY, eliminate))
              queue.append((newX, newY, eliminate, step + 1))
      return -1
    return bfs(grid)

sol = Solution()
assert sol.shortestPath(
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]],
k = 1) == 6

assert sol.shortestPath(
[[0,1,1],
 [1,1,1],
 [1,0,0]], 
k = 1) == -1

assert sol.shortestPath(
[[0,1,1],
 [1,1,1],
 [1,1,1],
 [1,1,1],
 [1,1,0]],
k = 5) == 6

assert sol.shortestPath(
[[0]],
k = 1) == 0

assert sol.shortestPath(
[[0],
 [0]],
k = 1) == 1

assert sol.shortestPath(
[[0,1],
 [1,0]],
k = 1) == 2

assert sol.shortestPath(
[[0,1,0,1],[0,1,0,0],[0,0,1,0],[1,0,0,1],[0,1,0,0]],
18) == 7



