from typing import List

class Solution:
  def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
    N = len(cars)
    ans = [-1 for _ in range(N)]
    stack = [N - 1] # N - 1 should always result in -1 as it is the top fleet one.
    for i in range(N - 2, -1, -1):
      _, speedI = cars[i]
      while stack and speedI <= cars[stack[-1]][1]: 
        # pop all cars which speed >= current speed
        # cur car can never reach this ahead car
        stack.pop()
      while stack and ans[stack[-1]] > 0 and (
              self.calcCollision(cars, stack[-1], cars[i]) >= ans[stack[-1]]):
        # Pop the cars that in same fleet (first one must be -1: slowest car in the fleet)
        # and if ahead car has collision time > current ahead car collision time in the result
        # pop it out and consider the next ahead car which for sure has smaller collision time.
        # [[3,4],[5,4],[6,3],[9,1]]
        # at the position 0, stack will have [3,2,1], ans is [-1, 1, 1.5, -1]
        # pos 0 has less speed than pos 1 => pop out
        # pos 0 has collision time vs pos 2 is 3 while ans[pos 2] is 1.5 => pop pos 2 out
        # ans[pos 3] is -1, it should be the remaining :)
        stack.pop()
      if stack:
        ans[i] = self.calcCollision(cars, stack[-1], cars[i])
      stack.append(i)
    # print(f'{ans}')
    return ans
  
  def calcCollision(self, cars, stackPeek, curCar):
    posI, speedI = curCar
    ans = round(float(cars[stackPeek][0] - posI) / (speedI - cars[stackPeek][1]), 5)
    # print(f'{ans}')
    return ans

  def getCollisionTimes_myVersion(self, cars: List[List[int]]) -> List[float]:
    '''
    Haven't finish
    '''
    ans = [-1 for _ in range(len(cars))]
    for i in range(len(cars) - 2, -1, -1):
      posI, speedI = cars[i]
      posIPlus1, speedIPlus1 = cars[i + 1]
      if speedI > speedIPlus1:
        ans[i] = float(posIPlus1 - posI) / (speedI - speedIPlus1)
        # cars[i][0] = ans[i] * speedIPlus1
        # cars[i][1] = speedIPlus1
    # print(f'{ans}')
    return ans
sol = Solution()
assert sol.getCollisionTimes([[1,2],[2,1],[4,3],[7,2]]) == [1.00000,-1.00000,3.00000,-1.00000]
assert sol.getCollisionTimes([[3,4],[5,4],[6,3],[9,1]]) == [2.00000,1.00000,1.50000,-1.00000]
assert sol.getCollisionTimes([[1,3],[4,1],[7,3],[10,5],[11,2],[13,5],[17,4],[20,1]]) == [1.50000,-1.00000,4.00000,0.33333,9.00000,1.75000,1.00000,-1.00000]
