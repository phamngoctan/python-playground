from typing import List

class Solution:
  def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    R = len(matrix)
    C = len(matrix[0])
    rowAffected = False
    colAffected = False
    for i in range(R):
      for j in range(C):
        if matrix[i][j] == 0:
          if i == 0:
            rowAffected = True
          if j == 0:
            colAffected = True
          matrix[i][0] = 0
          matrix[0][j] = 0
    for i in range(1, R):
      for j in range(1, C):
        if matrix[i][0] == 0 or matrix[0][j] == 0:
          matrix[i][j] = 0
    if rowAffected:
      for i in range(C):
        matrix[0][i] = 0
    if colAffected:
      for j in range(R):
        matrix[j][0] = 0
    # print(f'{matrix}')

sol = Solution()
arr = [[1,1,1],[1,0,1],[1,1,1]]
sol.setZeroes(arr)
assert arr == [[1,0,1],[0,0,0],[1,0,1]]

arr = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
sol.setZeroes(arr)
assert arr == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

arr = [[1,1,1,1]]
sol.setZeroes(arr)
assert arr == [[1,1,1,1]]

arr = [[0,1,2,0]]
sol.setZeroes(arr)
assert arr == [[0,0,0,0]]

arr = [[0,1],[1,1]]
sol.setZeroes(arr)
assert arr == [[0,0],[0,1]]

arr = [[0,0],[1,1]]
sol.setZeroes(arr)
assert arr == [[0,0],[0,0]]

arr = [[0]]
sol.setZeroes(arr)
assert arr == [[0]]

arr = [[1]]
sol.setZeroes(arr)
assert arr == [[1]]

arr = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
sol.setZeroes(arr)
assert arr == [[0,0,3,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

