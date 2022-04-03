from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mStack = [-1]
        heights.append(0)
        ans = 0
        for i in range(len(heights)):
            while mStack and heights[i] < heights[mStack[-1]]:
                height = heights[mStack.pop()]
                cur = height * (i - 1 - mStack[-1])
                ans = max(cur, ans)
            mStack.append(i)
        # print(f'{ans}')
        return ans

sol = Solution()
assert sol.largestRectangleArea([2,1,5,6,2,3]) == 10
assert sol.largestRectangleArea([1,1,1,1,1,2,2]) == 7