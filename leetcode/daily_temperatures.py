from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        daily_temp = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            if len(stack) == 0:
                stack.append(i)
            else:
                while len(stack) > 0 and T[stack[-1]] <= T[i]:
                    stack.pop()
                daily_temp[i] = 0 if len(stack) == 0 else stack[-1] - i
                stack.append(i)
        return daily_temp

s = Solution()
print("expect: [1, 1, 4, 2, 1, 1, 0, 0] and result is ", s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print("expect: [8,1,5,4,3,2,1,1,0,0] and result is ", s.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))
