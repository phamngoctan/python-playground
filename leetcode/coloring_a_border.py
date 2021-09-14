from typing import List

class Solution:
  def colorBorder(self, image: List[List[int]], row: int, col: int, newColor: int) -> List[List[int]]:
    oldColor = image[row][col]
    if oldColor == newColor:
      return image
    R, C = len(image), len(image[0])
    def isInvalid(x, y):
      return x < 0 or y < 0 or x >= R or y >= C
    direction = [[0,1],[0,-1],[1,0],[-1,0]]
    
    def dfs(image, pos, oldColor, newColor):
      image[pos[0]][pos[1]] = -oldColor
      for i in range(4):
        newX = pos[0] + direction[i][0]
        newY = pos[1] + direction[i][1]
        if isInvalid(newX, newY) or image[newX][newY] != oldColor:
          continue
        dfs(image, [newX, newY], oldColor, newColor)
      isInside = True
      for i in range(4):
        newX = pos[0] + direction[i][0]
        newY = pos[1] + direction[i][1]
        if isInvalid(newX, newY) or abs(image[newX][newY]) != oldColor:
          isInside = False
          break;
      if isInside:
        image[pos[0]][pos[1]] = oldColor
    
    dfs(image, [row, col], oldColor, newColor)

    for i in range(R):
      for j in range(C):
        if image[i][j] < 0:
          image[i][j] = newColor
    # print(f'{image}')
    return image

sol = Solution()
assert sol.colorBorder([[1,1,1],[1,1,5],[1,5,1]], 1, 1, 2) == [[2,2,2],[2,2,5],[2,5,1]]
assert sol.colorBorder([[1,1,5]], 0, 0, 3) == [[3,3,5]]
assert sol.colorBorder([[1,1,1],[1,1,1]], 0, 0, 2) == [[2,2,2],[2,2,2]]
assert sol.colorBorder([[1]], 0, 0, 3) == [[3]]
assert sol.colorBorder([[2,2,2],[2,1,1]], 1, 1, 1) == [[2,2,2],[2,1,1]]
assert sol.colorBorder([[1,1],[1,2]], 0, 0, 3) == [[3,3],[3,2]]
assert sol.colorBorder([[1,2,2],[2,3,2]], 0, 1, 3) == [[1,3,3],[2,3,3]]
assert sol.colorBorder([[1,1,1],[1,1,1],[1,1,1]], 1, 1, 2) == [[2,2,2],[2,1,2],[2,2,2]]
