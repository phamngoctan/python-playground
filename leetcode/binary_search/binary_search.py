from math import floor

def binary_search(arr, target):
  # if not arr:
  #   return -1
  left = 0;
  right = len(arr) - 1
  while left <= right: # in case the equal, means left = right and they are in the middle
    mid = floor((left + right) / 2) # instead of using floor, use operator //
    curValue = arr[mid]
    if curValue == target:
      return mid
    elif curValue < target:
      left = mid + 1
    else:
      right = mid - 1
  return -1

def binary_search_rightMost(nums, target):
  left, right = 0, len(nums) - 1
  pos = None
  while left <= right:
    mid = left + (right - left) // 2
    if (mid == right or target < nums[mid + 1]) and nums[mid] == target:
      pos = mid
      break
    elif target < nums[mid]:
      right = mid - 1
    else:
      left = mid + 1
  # print(f'{pos}')
  return pos if pos != None else -1

def binary_search_rightMostForInsert(nums, target):
  lo, hi = 0, len(nums) - 1
  while lo < hi:
    mid = (lo + hi + 1) // 2
    if nums[mid] > target:
      hi = mid - 1
    else:
      lo = mid
  return lo

def binary_search_leftMostForInsert(nums, target):
  # import bisect
  # return bisect.bisect_left(nums, target)
  lo, hi = 0, len(nums) # hi = len(nums) because target might > max value
  while lo < hi:
    mid = (lo + hi - 1) // 2
    if nums[mid] < target:
      lo = mid + 1
    else:
      hi = mid
  # print(f'{lo}')
  return lo

assert binary_search([1,2,3,4,5,6,7], 5) == 4
assert binary_search([], 10) == -1
assert binary_search_rightMost([1,2,2,2,3,4,5,6,7], 2) == 3
assert binary_search_rightMostForInsert([1,2,2,2,3,4,5,6,7], 2) == 3
assert binary_search_rightMostForInsert([1,2,2,2,4,5,6,7], 3) == 3
assert binary_search_rightMostForInsert([1,2,3,4,4,5,6,7], 3) == 2
assert binary_search_rightMostForInsert([1,2,2,2,4,5,6,7], 3) == 3
assert binary_search_rightMostForInsert([2,2,2,4,5,6,7], 1) == 0
assert binary_search_leftMostForInsert([1,1,2,2,2,4,5,6,7], 2) == 2
assert binary_search_leftMostForInsert([1,1,2,2,4,4,4,5,6,7], 3) == 4
assert binary_search_leftMostForInsert([1,6,7], 8) == 3
assert binary_search_leftMostForInsert([1,6,7,10], 11) == 4
