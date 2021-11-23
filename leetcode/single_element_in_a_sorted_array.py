from typing import List

class Solution:
  def singleNonDuplicate(self, nums):
    '''
    StefanPochmann - superman creates this idea
    '''
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] == nums[mid ^ 1]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]
  
  def singleNonDuplicate_theirFirstImprovement(self, nums: List[int]) -> int:
    '''
    Better than my idea, perform the -2 or + 2 for the new left,right
    '''
    left, right = 0, len(nums) - 1
    while left < right:
      mid = left + (right - left) // 2
      if (mid - left) % 2 == 0:
        if nums[mid] == nums[mid - 1]:
          right = mid - 2
        elif nums[mid] == nums[mid + 1]:
          left = mid + 2
        else:
          return nums[mid]
      else:
        if nums[mid] == nums[mid - 1]:
          left = mid + 1
        elif nums[mid] == nums[mid + 1]:
          right = mid - 1
        else:
          return nums[mid]
    # print(f'{nums[left]}')
    return nums[left]
  
  def singleNonDuplicate_myVersion(self, nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
      mid = left + (right - left) // 2
      if (mid - left) % 2 == 0:
        if nums[mid] == nums[mid - 1]:
          right = mid
        elif nums[mid] == nums[mid + 1]:
          left = mid
        else:
          return nums[mid]
      else:
        if nums[mid] == nums[mid - 1]:
          left = mid + 1
        elif nums[mid] == nums[mid + 1]:
          right = mid - 1
        else:
          return nums[mid]
    # print(f'{nums[left]}')
    return nums[left]
sol = Solution()
assert sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8]) == 2
assert sol.singleNonDuplicate([3,3,7,7,10,11,11]) == 10
assert sol.singleNonDuplicate([0,1,1]) == 0
assert sol.singleNonDuplicate([1,1,2]) == 2
assert sol.singleNonDuplicate([1,1,2,2,3,4,4]) == 3
assert sol.singleNonDuplicate([1,1,2,2,3,3,4,4,5]) == 5
assert sol.singleNonDuplicate([1,2,2,3,3,4,4,5,5]) == 1
assert sol.singleNonDuplicate([1,1,2,3,3,4,4]) == 2
