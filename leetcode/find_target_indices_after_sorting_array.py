from typing import List

class Solution:
  def targetIndices(self, nums: List[int], target: int) -> List[int]:
    '''
    O(n) approach
    '''
    countEqual = countLessThan = 0
    for i, num in enumerate(nums):
      if num < target:
        countLessThan += 1
      elif num == target:
        countEqual += 1
    ans = [i + countLessThan for i in range(countEqual)]
    # print(f'{ans}')
    return ans
  
  def targetIndices_2(self, nums: List[int], target: int) -> List[int]:
    '''
    Search last matched value
    '''
    nums.sort()
    left, right = 0, len(nums) - 1
    pos = -1
    while left <= right:
      mid = left + (right - left) // 2
      if (mid == right or target < nums[mid + 1]) and nums[mid] == target:
        pos = mid
        break
      elif target < nums[mid]:
        right = mid - 1
      else:
        left = mid + 1
    if pos == -1:
      return []
    tmp = pos
    ans = [tmp]
    while tmp > 0 and nums[tmp] == nums[tmp - 1]:
      tmp = tmp - 1
      ans.append(tmp)
    # print(f'{ans[::-1]}')
    return ans[::-1]
  
  def targetIndices_1(self, nums: List[int], target: int) -> List[int]:
    '''
    Search first matched value
    '''
    nums.sort()
    left, right = 0, len(nums) - 1
    pos = -1
    while left <= right:
      mid = left + (right - left) // 2
      if (mid == left or target > nums[mid - 1]) and nums[mid] == target:
        pos = mid
        break
      elif nums[mid] < target:
        left = mid + 1
      else:
        right = mid - 1
    if pos == -1:
      return []
    tmp = pos
    ans = [tmp]
    while tmp < len(nums) - 1 and nums[tmp] == nums[tmp + 1]:
        tmp = tmp + 1
        ans.append(tmp)
    # print(f'{ans}')
    return ans
sol = Solution()
assert sol.targetIndices([1,2,5,3], target = 9) == []
assert sol.targetIndices([1,2,5,2,3], target = 2) == [1,2]
assert sol.targetIndices([1,2,5,3], target = 2) == [1]
assert sol.targetIndices([2,2,2,2], target = 2) == [0,1,2,3]
assert sol.targetIndices([1,2,5,2,3,2,5,2], target = 2) == [1,2,3,4]
