from typing import List

class Solution:
  def sortedSquares(self, nums: List[int]) -> List[int]:
    left = 0
    right = len(nums) - 1
    res = []
    while left <= right:
      # print(f'{nums[left]} vs {nums[right]}')
      if pow(nums[right], 2) > pow(nums[left], 2):
        res.insert(0, pow(nums[right], 2))
        right -= 1
      else:
        res.insert(0, pow(nums[left], 2))
        left += 1
    # print(f'{res}')
    return res
sol = Solution()
assert sol.sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]
assert sol.sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]
assert sol.sortedSquares([-7]) == [49]