from typing import List
from heapq import heappush, heappop, heapreplace

class Solution:
  def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    def countLessOrQual(x):
      count = 0
      c = n - 1
      for r in range(n):
        while c >= 0 and matrix[r][c] > x:
          c -= 1
        count += c + 1
      return count
    
    left, right = matrix[0][0], matrix[n - 1][n - 1]
    ans = None
    while left <= right:
      mid = left + (right - left) // 2
      if countLessOrQual(mid) >= k:
        ans = mid
        right = mid - 1
      else:
        left = mid + 1
    return ans
  
  def kthSmallest_usingHeap_nlogk(self, matrix: List[List[int]], k: int) -> int:
    arr = []
    n = len(matrix)
    for i in range(n):
      for j in range(n):
        if len(arr) == n * n - k + 1:
          heapreplace(arr, matrix[i][j])
        else:
          heappush(arr, matrix[i][j])
    # print(f'{arr}')
    ans = heappop(arr)
    # print(f'{ans}')
    return ans
     
  def kthSmallest_playaround_still_be_accepted(self, matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    tmp = []
    for i in range(n):
      for j in range(n):
        tmp.append(matrix[i][j])
    tmp.sort()
    return tmp[k - 1]
sol = Solution()
assert sol.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], k = 8) == 13
assert sol.kthSmallest([[-5]], k = 1) == -5
