from typing import List

class Solution:
  def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
    maxItem = [releaseTimes[0], keysPressed[0]]
    for i in range(1, len(releaseTimes)):
      dis = releaseTimes[i] - releaseTimes[i - 1]
      if dis > maxItem[0] or (dis == maxItem[0] and keysPressed[i] > maxItem[1]):
        maxItem = [dis, keysPressed[i]]
    return maxItem[1]

sol = Solution()
assert sol.slowestKey([9,29,49,50], "cbcd") == 'c'
assert sol.slowestKey([12,23,36,46,62], "spuda") == 'a'