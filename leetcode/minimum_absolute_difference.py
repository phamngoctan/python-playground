from typing import List

class Solution:
  def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
    arr.sort()
    ans = []
    minAbsDiff = float('inf')
    for i in range(1, len(arr)):
      absDiff = arr[i] - arr[i - 1]
      if absDiff < minAbsDiff:
        minAbsDiff = absDiff
        ans = []
        ans.append([arr[i - 1], arr[i]])
      elif absDiff == minAbsDiff:
        ans.append([arr[i - 1], arr[i]])
    return ans
  
  def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
    '''
    Time complexity O(n^2)
    '''
    ans = []
    minAbsDiff = float('inf')
    for i in range(len(arr)):
      for j in range(i + 1, len(arr)):
        absDiff = abs(arr[j] - arr[i])
        if absDiff < minAbsDiff:
          minAbsDiff = absDiff
          ans = []
          ans.append(sorted([arr[i], arr[j]]))
        elif absDiff == minAbsDiff:
          ans.append(sorted([arr[i], arr[j]]))
    return sorted(ans)
sol = Solution()
assert sol.minimumAbsDifference([4,2,1,3]) == [[1,2],[2,3],[3,4]]
assert sol.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]) == [[-14,-10],[19,23],[23,27]]
assert sol.minimumAbsDifference([1,3,6,10,15]) == [[1,3]]