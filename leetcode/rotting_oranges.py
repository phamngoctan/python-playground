from typing import List

class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
    direction = [[0,1],[0,-1],[-1,0],[1,0]]
    R = len(grid)
    C = len(grid[0])
    def bfs(grid, rottedPos):
      queue = rottedPos
      level = 0
      while queue:
        size = len(queue)
        level += 1
        for _ in range(size):
          cur = queue.pop(0)
          # print(f'at level {level - 1}: {cur}')
          for i in range(4):
            newX = cur[0] + direction[i][0]
            newY = cur[1] + direction[i][1]
            if isNotValid(newX, newY) or grid[newX][newY] != 1:
              continue
            # print(f'at level {level - 1}: {[newX, newY]} added value {grid[newX][newY]}')
            grid[newX][newY] = -2
            queue.append([newX, newY])
        # print(f'grid is {grid}')
      return level - 1
    def isNotValid(x, y):
      return x < 0 or y < 0 or x >= R or y >= C
    
    rottedPos = []
    for i in range(R):
      for j in range(C):
        if grid[i][j] == 2:
          rottedPos.append([i,j])
          grid[i][j] = -2
    maxTime = 0 if not rottedPos else bfs(grid, rottedPos)
    
    # print(f'{maxTime}')
    # print(f'{grid}')
    for i in range(R):
      for j in range(C):
        if grid[i][j] == 1:
          return -1
    return maxTime

sol = Solution()
assert sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
assert sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
assert sol.orangesRotting([[0,2]]) == 0
assert sol.orangesRotting([
  [2,1,1],
  [1,1,1],
  [0,1,2]]) == 2
assert sol.orangesRotting([[0]]) == 0
assert sol.orangesRotting([[2,2],[1,1],[0,0],[2,0]]) == 1
