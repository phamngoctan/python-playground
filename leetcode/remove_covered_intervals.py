from typing import List

class Solution:
    def removeCoveredIntervals_myIdea(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(f'{intervals}')
        # for i in range(len(intervals) - 1):
        ans = len(intervals)
        # print(f'{ans}')
        curStart, curEnd = intervals[0]
        i = 1
        while i < len(intervals):
            nextStart, nextEnd = intervals[i]
            if nextEnd >= curEnd and nextStart == curStart: # cur cover next item
                ans -= 1
                curEnd = nextEnd
            elif curEnd >= nextEnd:
                ans -= 1
            else:
                curStart, curEnd = intervals[i]
            i += 1
        print(f'{ans}')
        return ans
    
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """A cleaner idea"""
        # newIntervals = sorted(intervals, key= lambda i: (i[0], -i[1]))
        intervals.sort(key= lambda i: (i[0], -i[1]))
        # print(f'{intervals}')
        ans = cur = 0
        for _, end in intervals:
            if cur < end:
                ans += 1
                cur = end
        return ans

sol = Solution()
assert sol.removeCoveredIntervals([[1,4],[2,8],[2,6]]) == 2
assert sol.removeCoveredIntervals([[1,4],[3,6],[2,8]]) == 2
assert sol.removeCoveredIntervals([[1,2],[1,4],[3,4]]) == 1
