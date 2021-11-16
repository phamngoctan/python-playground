from typing import List

class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    # print(f'{intervals}')
    res = [intervals[0]]
    for i in range(1, len(intervals)):
      if res[-1][1] > intervals[i][1]:
        continue
      if res[-1][1] >= intervals[i][0]:
        res[-1][1] = intervals[i][1]
      else:
        res.append(intervals[i])
    # print(f'{res}')
    return res
sol = Solution()
assert sol.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
assert sol.merge([[3,4],[4,5],[1,6]]) == [[1,6]]
assert sol.merge([[2,4],[1,5]]) == [[1,5]]
assert sol.merge([[1,4],[4,5]]) == [[1,5]]
assert sol.merge([[4,5],[1,4]]) == [[1,5]]
assert sol.merge([[1,4]]) == [[1,4]]
