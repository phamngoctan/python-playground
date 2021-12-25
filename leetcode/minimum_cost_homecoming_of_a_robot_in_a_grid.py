from typing import List
from queue import PriorityQueue

class Solution:
  def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
    res = 0
    i, j = startPos
    endX, endY = homePos
    while i != endX:
      i += (endX - i) // abs(endX - i)
      res += rowCosts[i]
    while j != endY:
      j += (endY - j) // abs(endY - j)
      res += colCosts[j]
    return res
  
  '''
  The problem is easier than I thought :|
  '''
  def minCost_TLE(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
    R, C = len(rowCosts), len(colCosts)
    DIR = [[0,1],[1,0],[-1,0],[0,-1]]
    dist = [[float('inf') for _ in range(C)] for _ in range(R)]
    def valid(x, y):
      return x >= 0 and x < R and y >= 0 and y < C
    pq = PriorityQueue()
    pq.put([0, startPos[0], startPos[1]])
    dist[startPos[0]][startPos[1]] = 0
    while pq.qsize() > 0:
      curDist, curX, curY = pq.get()
      if curX == homePos[0] and curY == homePos[1]:
        return dist[curX][curY]
      if curDist > dist[curX][curY]:
        continue
      for x, y in DIR:
        newX = x + curX
        newY = y + curY
        if valid(newX, newY):
          newDist = curDist + (colCosts[newY] if x == 0 else rowCosts[newX])
          if newDist < dist[newX][newY]:
            dist[newX][newY] = newDist
            pq.put([newDist, newX, newY])
    return 0
sol = Solution()
assert sol.minCost([1, 0], homePos = [2, 3], rowCosts = [5, 4, 3], colCosts = [8, 2, 6, 7]) == 18
assert sol.minCost([0, 0], homePos = [0, 0], rowCosts = [5], colCosts = [26]) == 0
# [[5, 5, 5, 12], 
#  [0, 2, 4, 11], 
#  [3, 3, 3, 10]]