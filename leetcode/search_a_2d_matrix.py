from typing import List

class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    R = len(matrix)
    C = len(matrix[0])
    left = 0
    right = R * C - 1
    while (left <= right):
      mid = (left + right) // 2
      # x = mid//C
      # y = mid%C
      # print(f'{x},{y} val: {matrix[x][y]}')
      val = matrix[mid//C][mid%C]
      if val == target:
        return True
      elif val < target:
        left = mid + 1
      else:
        right = mid - 1
    return False
sol = Solution()
assert sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True
assert sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13) == False
assert sol.searchMatrix([[1]], 1) == True
assert sol.searchMatrix([[1,2,3,4,5]], 3) == True
