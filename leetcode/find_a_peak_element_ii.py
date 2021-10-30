from typing import List

class Solution:
  def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
    left = 0
    right = len(mat)-1
    while left < right:
      mid = left + (right - left) // 2
      if max(mat[mid]) > max(mat[mid + 1]):
        right = mid
      else:
        left = mid + 1
    # print(right)
    return [right, mat[right].index(max(mat[right]))]
sol = Solution()
assert sol.findPeakGrid([[1,4],[3,2]]) == [0,1]
assert sol.findPeakGrid([[10,20,15],[21,30,14],[7,16,32]]) == [2,2]
assert sol.findPeakGrid([[10,20,32],[21,30,14],[7,16,15]]) == [0,2]
