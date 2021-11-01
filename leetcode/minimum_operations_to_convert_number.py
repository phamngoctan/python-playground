from typing import List

class Solution:
  def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
    def bfs(nums, start, goal):
      queue = [start]
      visited = set([start])
      level = 0
      while len(queue) > 0:
        level += 1
        queueSize = len(queue)
        for _ in range(queueSize):
          cur = queue.pop(0)
          for num in nums:
            allOperations = [cur + num, cur - num, cur ^ num]
            for opt in allOperations:
              if opt == goal:
                # print(f'{level}')
                return level
              if not opt in visited and isValid(opt):
                queue.append(opt)
                visited.add(opt)
      # print(f'-1')
      return -1
    def isValid(x):
      return x >= 0 and x <= 1000
    return bfs(nums, start, goal)
sol = Solution()
assert sol.minimumOperations([1,3], start = 6, goal = 4) == 2
assert sol.minimumOperations([2,4,12], start = 2, goal = 12) == 2
assert sol.minimumOperations([3,5,7], start = 0, goal = -4) == 2
assert sol.minimumOperations([2,8,16], start = 0, goal = 1) == -1
assert sol.minimumOperations([1], start = 0, goal = 3) == 3
