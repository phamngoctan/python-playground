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

assert binary_search([1,2,3,4,5,6,7], 5) == 4
assert binary_search([], 10) == -1