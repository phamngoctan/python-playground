from typing import List

class Solution:
  '''
  visited set not work because the worse case is there is no duplicated newVal
  '''
  def minOperations(self, nums: List[int], x: int) -> int:
    def bfs(nums, x):
      queue = [(x, 0,len(nums) - 1)]
      visited = set([(x, 0, len(nums) - 1)])
      level = 0
      while len(queue) > 0:
        level += 1
        queueLength = len(queue)
        for _ in range(queueLength):
          val, left, right = queue.pop(0)
          newVal = val - nums[left]
          if newVal == 0:
            return level
          if not (newVal, left + 1, right) in visited and isValid(newVal, left + 1, right):
            queue.append((newVal, left + 1, right))
            visited.add((newVal, left + 1, right))
          newVal = val - nums[right]
          if newVal == 0:
            # print(f'{level}')
            return level
          if not (newVal, left, right - 1) in visited and isValid(newVal, left, right - 1):
            queue.append((newVal, left, right - 1))
            visited.add((newVal, left, right - 1))
      return -1
    def isValid(val, left, right):
      return val >= 0 and left <= right
    return bfs(nums, x)


sol = Solution()
assert sol.minOperations([1,1,4,2,3], x = 5) == 2
assert sol.minOperations([5,6,7,8,9], x = 4) == -1
assert sol.minOperations([3,2,20,1,1,3], x = 10) == 5
assert sol.minOperations([1,1], x = 2) == 2
assert sol.minOperations([1,1,4], x = 6) == 3
assert sol.minOperations([8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309], x = 134365) == 16
