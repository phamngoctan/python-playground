from typing import List

class Solution:
  def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    for i in range(len(nums)):
      if nums[abs(nums[i]) - 1] > 0:
        nums[abs(nums[i]) - 1] *= -1
    # print(f'{nums}')
    res = []
    for i in range(len(nums)):
      if nums[i] > 0:
        res.append(i + 1)
    return res
  def findDisappearedNumbers_notGood(self, nums: List[int]) -> List[int]:
    tmp = [0 for i in range(len(nums))] 
    # print(f'{tmp}')
    for i in range(len(nums)):
      tmp[nums[i] - 1] += 1
    res = []
    for i in range(len(tmp)):
      if tmp[i] == 0:
        res.append(i + 1)
    return res
sol = Solution()
assert sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]) == [5,6]
assert sol.findDisappearedNumbers([1,1]) == [2]
assert sol.findDisappearedNumbers([1,2]) == []
