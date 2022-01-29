from typing import List
from collections import deque

class Solution:
  def sequentialDigits(self, low: int, high: int) -> List[int]:
    """ Using BFS idea, one queue
    """
    queue = deque([1,2,3,4,5,6,7,8,9])
    ans = []
    while len(queue):
      cur = queue.popleft()
      if cur > high: break
      if low <= cur <= high: ans.append(cur)
      if cur % 10 == 9:
        continue
      queue.append(cur * 10 + cur % 10 + 1)
    return ans
  
  def sequentialDigits_needSorting(self, low: int, high: int) -> List[int]:
    """Borrow idea from LC
    Start with digits 1,2,3,4,5,6,7,8
    Time complexity O(nlogn) (n is the total number of 12,23,34,...,123456789)
    """
    def dfs(cur, low, high):
      if cur > high: return
      if cur >= low: ans.append(cur)
      if cur % 10 == 9: return # break when 89, 789, 6789, 56789, ..., 123456789
      next = cur * 10 + cur % 10 + 1
      dfs(next, low, high)
    
    ans = []
    for i in range(1, 9):
      dfs(i, low, high)
    # print(f'{sorted(ans)}')
    return sorted(ans)
    
sol = Solution()
assert sol.sequentialDigits(10, 300) == [12, 23, 34, 45, 56, 67, 78, 89, 123, 234]
assert sol.sequentialDigits(100, 300) == [123,234]
assert sol.sequentialDigits(1000, high = 13000) == [1234,2345,3456,4567,5678,6789,12345]
