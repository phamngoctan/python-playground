from typing import List

class Solution:
  def minEatingSpeed(self, piles: List[int], h: int) -> int:
    left, right = 1, max(piles)
    while left <= right:
      mid = left + (right - left) // 2
      if self.canEatAll(piles, mid, h):
        right = mid - 1
      else:
        left = mid + 1
    # print(f'{left}')
    return left
  def canEatAll(self, piles, speed, withinHours):
    count = 0
    for bananas in piles:
      count += bananas // speed
      if bananas % speed:
        count += 1
    return count <= withinHours

sol = Solution()
assert sol.minEatingSpeed([3,6,7,11], h = 8) == 4
