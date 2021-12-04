from typing import List

class Solution:
  def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
    R, C = len(land), len(land[0])
    DIRECTION = [[0,1],[1,0]]
    def valid(x, y):
      return x >= 0 and x < R and y >= 0 and y < C
    def DFS(cell):
      global maxX, maxY
      curX, curY = cell
      land[curX][curY] = 0
      for x, y in DIRECTION:
        newX = curX + x
        newY = curY + y
        if not valid(newX, newY) or not land[newX][newY]:
          continue
        maxX = max(maxX, newX)
        maxY = max(maxY, newY)
        DFS([newX, newY])
      
    ans = []
    i, j = 0, 0
    global maxX, maxY
    while i < R and j < C:
      if land[i][j] == 1:
        maxX, maxY = i, j
        DFS([i, j])
        ans.append([i, j, maxX, maxY])
      if j == C - 1:
        i += 1
        j = 0
      else:
        j += 1
    # print(f'{ans}')
    return ans

sol = Solution()
assert sol.findFarmland([[1,0,0],[0,1,1],[0,1,1]]) == [[0,0,0,0],[1,1,2,2]]
assert sol.findFarmland([[1,1],[1,1]]) == [[0,0,1,1]]
