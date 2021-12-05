from typing import List
import queue

class Solution:
  def swimInWater(self, grid: List[List[int]]) -> int:
    '''
    Main idea: use PriorityQueue and go with the smallest path until the bottom right position
    '''
    R, C = len(grid), len(grid[0])
    DIRECTION = [[0,1],[1,0],[0,-1],[-1,0]]
    visited = [[False for _ in range(C)] for _ in range(R)]
    def valid(x, y):
      return x >= 0 and x < R and y >= 0 and y < C
    pqueue = queue.PriorityQueue()
    pqueue.put([grid[0][0], 0, 0])
    visited[0][0] = True
    ans = 0
    while pqueue.qsize() > 0:
      curVal, curX, curY = pqueue.get()
      ans = max(ans, curVal)
      if curX == curY == R - 1:
        return ans
      for x, y in DIRECTION:
        newX = x + curX
        newY = y + curY
        if not valid(newX, newY) or visited[newX][newY]:
          continue
        visited[newX][newY] = True
        pqueue.put([grid[newX][newY], newX, newY])
      
  def swimInWater_TLE(self, grid: List[List[int]]) -> int:
    '''
    TLE because of the time complexity: O(4^n^2)
    '''
    R, C = len(grid), len(grid[0])
    DIRECTION = [[0,1],[1,0],[0,-1],[-1,0]]
    visited = [[False for _ in range(C)] for _ in range(R)]
    def valid(x, y):
      return x >= 0 and x < R and y >= 0 and y < C
    def DFS(grid, cell, maxSoFarInCurPath):
      global minTime
      curX, curY = cell
      if curX == R - 1 and curY == C - 1:
        minTime = min(maxSoFarInCurPath, minTime)
      for x, y in DIRECTION:
        newX = x + curX
        newY = y + curY
        if not valid(newX, newY) or visited[newX][newY]:
          continue
        visited[newX][newY] = True
        newTime = max(grid[newX][newY], maxSoFarInCurPath)
        DFS(grid, [newX, newY], newTime)
        visited[newX][newY] = False
      
    global minTime
    minTime = float('INF')
    visited[0][0] = True
    DFS(grid, [0, 0], grid[0][0])
    print(f'{minTime}')
    return minTime
sol = Solution()
# assert sol.swimInWater([[0,2],[1,3]]) == 3
# assert sol.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]) == 16
# assert sol.swimInWater([[0,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]) == 11
# assert sol.swimInWater([[0,13,14,15,16],[10,9,8,7,6]]) == 10
# assert sol.swimInWater([[10,13],[7,6]]) == 10
# assert sol.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16]]) == 16
# assert sol.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20]]) == 20
# assert sol.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20]]) == 20
# assert sol.swimInWater([[0,1,2,3,4,5,16,15,14,13,12,11,10,9,8,7,6]]) == 16
# assert sol.swimInWater([[3,2],[0,1]]) == 3
# assert sol.swimInWater([[10,12,4,6],
#                         [9,11,3,5],
#                         [1,7,13,8],
#                         [2,0,15,14]]) == 14
assert sol.swimInWater([[35,19,17,25,4,10],[8,18,29,21,28,31],[15,5,33,2,13,3],[26,20,27,23,11,1],[6,14,24,7,12,16],[30,34,32,22,0,9]]) == 35
