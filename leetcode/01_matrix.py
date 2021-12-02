from typing import List

class Solution:
  def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    R, C = len(mat), len(mat[0])
    DIRECTION = [[0,1],[1,0],[-1,0],[0,-1]]
    def valid(x, y):
      return x >= 0 and x < R and y >= 0 and y < C
    
    def BFS(mat, queue):
      while len(queue) > 0:
        curX, curY = queue.popleft()
        for x,y in DIRECTION:
          newX = curX + x
          newY = curY + y
          if not valid(newX, newY) or mat[newX][newY] >= 0:
            continue
          mat[newX][newY] = mat[curX][curY] + 1
          queue.append([newX, newY])

    import collections
    queue = collections.deque([])
    for i in range(R):
      for j in range(C):
        if mat[i][j] > 0:
          mat[i][j] = -1
        else:
          queue.append([i, j])
    BFS(mat, queue)
    # print(mat)
    return mat

sol = Solution()
assert sol.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]) == [[0,0,0],[0,1,0],[0,0,0]]
assert sol.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]) == [[0,0,0],[0,1,0],[0,0,0]]
assert sol.updateMatrix([[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]]) == [[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]]
