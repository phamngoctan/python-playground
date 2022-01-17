from typing import List

class Solution:
  def maxDistToClosest(self, seats: List[int]) -> int:
    prevPos = None
    ans = 1
    for i in range(len(seats)):
      if seats[i] == 1:
        if prevPos == None: # handle empty start chair
          ans = i
        else:
          ans = max(ans, (i - prevPos) // 2)
        prevPos = i
    ans = max(ans, len(seats) - prevPos - 1) # handle empty end chair
    return ans

  def maxDistToClosest_nonCleanVersion(self, seats: List[int]) -> int:
    """ Time complexity is O(n) but the code is not clean
    """
    ans = 1 # base on condition, this is the minimum answer
    ans = self.getMaxDistInCaseEmptyStartChair(seats)
    ans = max(self.getMaxDistInCaseEmptyEndChair(seats), ans)
    # print(f'{ans}')
    seats = [1] + seats + [1]
    prevPos = 0
    for i in range(1, len(seats)):
      if seats[i] == 1:
        ans = max((i - prevPos) // 2, ans)
        prevPos = i
    # print(f'{ans}')
    return ans

  def getMaxDistInCaseEmptyEndChair(self, seats):
    N = len(seats)
    if seats[-1] == 0: # in case [1,0,0,0] => 3 should be return
      i = N - 1
      while seats[i] == 0:
        i -= 1
      return N - i - 1
    return 0

  def getMaxDistInCaseEmptyStartChair(self, seats):
    if seats[0] == 0: # in case [0,0,0,1] => 3 should be return
      i = 0
      while seats[i] == 0:
        i += 1
      return i
    return 0
  
  def maxDistToClosest_bruceforce(self, seats: List[int]) -> int:
    """Bruceforce time complexity O(n^2)
    """
    ans = float('-inf')
    for i in range(len(seats)):
      if seats[i] == 0:
        closestDis = float('inf')
        for j in range(len(seats)):
          if seats[j] == 1:
            closestDis = min(closestDis, abs(j - i))
        ans = max(closestDis, ans)
    print(f'{ans}')
    return ans

sol = Solution()
assert sol.maxDistToClosest([1,0,0,0,1,0,1]) == 2
assert sol.maxDistToClosest([1,0,0,0]) == 3
assert sol.maxDistToClosest([1,0]) == 1
assert sol.maxDistToClosest([0,1]) == 1
assert sol.maxDistToClosest([0,0,0,0,1]) == 4
assert sol.maxDistToClosest([1,0,1]) == 1
assert sol.maxDistToClosest([1,0,0,0,0,1]) == 2
assert sol.maxDistToClosest([0,1,0,0,1,1,1,0,0,1,1,0,0,0,0,1]) == 2
