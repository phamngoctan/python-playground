from typing import List

class Solution:
  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    monotonicStack = []
    res = [0 for _ in range(len(temperatures))]
    for i, temp in enumerate(temperatures):
      while len(monotonicStack) > 0 and monotonicStack[-1][0] < temp:
        # dict[monotonicStack.pop()] = i
        prePos = monotonicStack.pop()[1]
        res[prePos] = i - prePos
      monotonicStack.append([temp, i])
    # print(f'{dict}')
    
    # for i, temp in enumerate(temperatures):
    #   if temp in dict and dict[temp] > i:
    #     res.append(dict.get(temp) - i)
    #   else:
    #     res.append(0)
    # print(f'{res}')
    return res
sol = Solution()
assert sol.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
assert sol.dailyTemperatures([30,40,50,60]) == [1,1,1,0]
assert sol.dailyTemperatures([34,80,80,34,34,80,80,80,80,34]) == [1,0,0,2,1,0,0,0,0,0]
