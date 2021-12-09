from typing import List
import queue 
from heapq import heappop, heappush

class Solution:
  def minimumEffortPath1(self, heights):
      m, n = len(heights), len(heights[0])
      dist = [[float('inf')] * n for _ in range(m)]
      minHeap = [(0, 0, 0)] # distance, row, col
      DIR = [0, 1, 0, -1, 0]
      while minHeap:
          d, r, c = heappop(minHeap)
          if d > dist[r][c]: continue
          if r == m - 1 and c == n - 1:
              print(f'{dist}')
              return d  # Reach to bottom right
          for i in range(4):
              nr, nc = r + DIR[i], c + DIR[i + 1]
              if 0 <= nr < m and 0 <= nc < n:
                  newDist = max(d, abs(heights[nr][nc] - heights[r][c]))
                  if dist[nr][nc] > newDist:
                      dist[nr][nc] = newDist
                      heappush(minHeap, (dist[nr][nc], nr, nc))
  
  def minimumEffortPath(self, heights: List[List[int]]) -> int:
    R, C = len(heights), len(heights[0])
    DIRECTION = [[0,1],[1,0],[-1,0],[0,-1]]
    def valid(x, y):
      return x >= 0 and x < R and y >= 0 and y < C
    ans = 0
    pqueue = queue.PriorityQueue()
    dist = [[float('inf') for _ in range(C)] for _ in range(R)]
    dist[0][0] = 0
    pqueue.put([0,0,0])
    while pqueue.qsize() > 0:
      gap, curX, curY = pqueue.get()
      if gap > dist[curX][curY]: continue
      ans = max(ans, gap)
      if curX == R - 1 and curY == C - 1:
        # print(f'{gap}')
        print(f'{dist}')
        return ans
      for x, y in DIRECTION:
        newX, newY = curX + x, curY + y
        if not valid(newX, newY):
          continue
        newDist = abs(heights[newX][newY] - heights[curX][curY])
        if newDist < dist[newX][newY]:
          dist[newX][newY] = newDist
          pqueue.put([newDist, newX, newY])
    
  def minimumEffortPath_bruceforce(self, heights: List[List[int]]) -> int:
    '''
    Bruce force, backtracking, not work because of TLE,
    Time complexity: O(3^n)
    '''
    R, C = len(heights), len(heights[0])
    DIRECTION = [[0,1],[1,0],[-1,0],[0,-1]]
    def valid(x, y):
      return x >= 0 and x < R and y >= 0 and y < C
    def DFS(cell, maxDiffCurrentPath):
      global ans
      curX, curY = cell
      val = heights[curX][curY]
      if curX == R - 1 and curY == C - 1:
        ans = min(maxDiffCurrentPath, ans)
      heights[curX][curY] = -1
      for x, y in DIRECTION:
        newX = x + curX
        newY = y + curY
        if not valid(newX, newY) or heights[newX][newY] == -1:
          continue
        DFS([newX, newY], max(heights[newX][newY] - val, maxDiffCurrentPath))
      heights[curX][curY] = val
    global ans
    ans = 10**6 + 5
    import time
    start = time.process_time()
    DFS([0,0], 0)
    print(f'{ans}')
    print(f'Time consuming {time.process_time() - start}')
    return ans
sol = Solution()
assert sol.minimumEffortPath([[3]]) == 0
assert sol.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]) == 2
assert sol.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]) == 1
assert sol.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]) == 0
assert sol.minimumEffortPath([[4,3,4,10,5,5,9,2],[10,8,2,10,9,7,5,6],[5,8,10,10,10,7,4,2],[5,1,3,1,1,3,1,9],[6,4,10,6,10,9,4,6]]) == 5
