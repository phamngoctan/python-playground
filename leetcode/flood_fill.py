from typing import List

class Solution:
  def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    oldColor = image[sr][sc]
    if oldColor == newColor:
      return image
    R, C = len(image), len(image[0])
    def isInvalid(x, y):
      return x < 0 or y < 0 or x >= R or y >= C
    direction = [[0,1],[0,-1],[1,0],[-1,0]]
    def dfs(image, pos, oldColor, newColor):
      image[pos[0]][pos[1]] = newColor
      for i in range(4):
        newX = pos[0] + direction[i][0]
        newY = pos[1] + direction[i][1]
        if isInvalid(newX, newY) or image[newX][newY] != oldColor:
          continue
        dfs(image, [newX, newY], oldColor, newColor)
    dfs(image, [sr, sc], oldColor, newColor)
    # print(f'{image}')
    return image

sol = Solution()
assert sol.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2) == [[2,2,2],[2,2,0],[2,0,1]]
assert sol.floodFill([[1,1,0]], 0, 0, 3) == [[3,3,0]]
assert sol.floodFill([[0,0,0],[0,0,0]], 0, 0, 1) == [[1,1,1],[1,1,1]]
assert sol.floodFill([[1]], 0, 0, 3) == [[3]]
assert sol.floodFill([[0,0,0],[0,1,1]], 1, 1, 1) == [[0,0,0],[0,1,1]]
