from typing import List

class Solution:
  def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    cars = sorted(list(zip(position, speed)))
    # print(f'{cars}')
    finishTimes = [0 for _ in range(len(position))]
    for i in range(len(position)):
      # without float the number
      # test case 10, position = [6,8], speed = [3,2] will be failed
      # due to the // resulted in integer [1,1] => only one fleet
      # while it requires 2 fleets, 8 finished first
      finishTimes[i] = (target - cars[i][0]) / float(cars[i][1])
    # print(f'{finishTime}')
    stack = []
    for time in finishTimes:
      while stack and stack[-1] <= time:
        stack.pop()
      stack.append(time)
    # print(f'{stack}')
    return len(stack)

  def carFleet_shorterVersion(self, target: int, position: List[int], speed: List[int]) -> int:
    cars = sorted(list(zip(position, speed)))
    stack = []
    for i in range(len(position)):
      time = (target - cars[i][0]) / float(cars[i][1])
      while stack and stack[-1] <= time:
        stack.pop()
      stack.append(time)
    return len(stack)
  
sol = Solution()
assert sol.carFleet(12, position = [10,8,0,5,3], speed = [2,4,1,1,3]) == 3
assert sol.carFleet(10, position = [3], speed = [3]) == 1
assert sol.carFleet(3, position = [3], speed = [3]) == 1
assert sol.carFleet(10, position = [6,8], speed = [3,2]) == 2
