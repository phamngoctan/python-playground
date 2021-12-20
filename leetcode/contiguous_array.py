from typing import List

class Solution:
  def findMaxLength(self, nums: List[int]) -> int:
    hash = {0:-1}
    count = 0
    maxLength = 0
    for i, val in enumerate(nums):
      count += 1 if val else -1
      # print(f'{count}')
      if count in hash:
        # print(f'hehe in hash {i - hash[count]}')
        maxLength = max(maxLength, i - hash[count])
      else:
        hash[count] = i
    # print(f'{maxLength}')
    return maxLength

sol = Solution()
assert sol.findMaxLength([0,1]) == 2
assert sol.findMaxLength([0,1,0]) == 2
assert sol.findMaxLength([0,1,1,1,1,0,1,0,1]) == 4
assert sol.findMaxLength([0,1,1,1,0,0,1,0,1]) == 8
assert sol.findMaxLength([0,1,0,0,0,1,0,1,1,1,1,0]) == 12
