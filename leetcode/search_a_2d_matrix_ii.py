from typing import List

class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    '''
    Adaptive search for 2D sorted in row and column array
    '''
    R, C = len(matrix), len(matrix[0])
    row, col = 0, C - 1
    while row < R and col >= 0:
      if matrix[row][col] == target:
        return True
      elif matrix[row][col] < target:
        row += 1
      else:
        col -= 1
    return False
  
  def searchMatrix_firstImprovement(self, matrix: List[List[int]], target: int) -> bool:
    '''
    Classic binary search for every row
    '''
    R, C = len(matrix), len(matrix[0])
    for row in range(R):
      left, right = 0, C - 1
      while left <= right:
        mid = left + (right - left)//2
        if matrix[row][mid] == target:
          return True
        elif matrix[row][mid] < target:
          left = mid + 1
        else:
          right = mid - 1
    return False
  
  def searchMatrix_bruceforce(self, matrix: List[List[int]], target: int) -> bool:
    R, C = len(matrix), len(matrix[0])
    for i in range(R):
      for j in range(C):
        if matrix[i][j] == target:
          return True
    return False
sol = Solution()
assert sol.searchMatrix([[1]], 1) == True
assert sol.searchMatrix([[1]], 9) == False
assert sol.searchMatrix([[1],[2]], 0) == False
assert sol.searchMatrix([[1],[5]], 1) == True
assert sol.searchMatrix([[1,4,7],[2,5,8]], 3) == False
assert sol.searchMatrix([[1,4,7],[2,5,8]], 5) == True
assert sol.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5) == True
assert sol.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20) == False
assert sol.searchMatrix([[1,4,7,11,15],[2,5,8,12,19]], 10) == False
assert sol.searchMatrix([[1,4,7,11,15],[2,5,8,12,19]], 11) == True
