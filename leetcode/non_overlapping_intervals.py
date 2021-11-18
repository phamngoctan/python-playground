from typing import List

class Solution:
  def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    '''
    Best approach
    '''
    intervals = sorted(intervals, key=lambda x: x[1])
    print(f'{intervals}')
    end, count = float('-inf'), 0
    for s, e in intervals:
      if s >= end:
        end = e
      else: 
        count += 1
    return count

  def eraseOverlapIntervals_improve1(self, intervals: List[List[int]]) -> int:
    '''
    Better approach, just store only the end
    '''
    intervals.sort()
    last = intervals[0][1]
    count = 0
    for i in range(1, len(intervals)):
      if last > intervals[i][1]:
        count += 1
        last = intervals[i][1]
        continue
      if last > intervals[i][0]:
        count += 1
      else:
        last = intervals[i][1]
    # print(f'{count}')
    return count

  def eraseOverlapIntervals_mySolution(self, intervals: List[List[int]]) -> int:
    intervals.sort()
    last = intervals[0]
    count = 0
    for i in range(1, len(intervals)):
      if last[1] > intervals[i][1]:
        count += 1
        last = intervals[i]
        continue
      if last[1] > intervals[i][0]:
        count += 1
      else:
        last = intervals[i]
    # print(f'{count}')
    return count
sol = Solution()
# assert sol.eraseOverlapIntervals([[1,3],[2,4],[5,6]]) == 1
# assert sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1
assert sol.eraseOverlapIntervals([[2,3],[3,4],[2,4],[1,6]]) == 2
assert sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[1,4]]) == 2
assert sol.eraseOverlapIntervals([[1,2],[2,3]]) == 0
assert sol.eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2
assert sol.eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]) == 2
