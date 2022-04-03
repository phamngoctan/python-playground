from typing import List
from heapq import heappush, heappop

class Solution:
    def minimumDeviation_votrubac(self, nums: List[int]) -> int:
        ans = minN = float('inf')
        heap = []
        for num in nums:
            evenNum = num if num % 2 == 0 else num * 2
            minN = min(minN, evenNum)
            heappush(heap, -evenNum)
        print(f'{heap}')
        while heap and heap[0] % 2 == 0:
            largest = -heap[0]
            ans = min(ans, largest - minN)
            minN = min(minN, largest//2)
            heappop(heap)
            heappush(heap, -(largest//2))
        print(f'{heap}')
        print(f'{ans}')
        return min(ans, -heap[0] - minN)
    
    def minimumDeviation(self, nums: List[int]) -> int:
        ans = minN = float('inf')
        heap = []
        for num in nums:
            evenNum = num if num % 2 == 0 else num * 2
            minN = min(minN, evenNum)
            heappush(heap, -evenNum)
        # print(f'{heap}')
        while heap:
            largest = -heap[0]
            ans = min(ans, largest - minN)
            minN = min(minN, largest//2)
            heappop(heap)
            if largest % 2 == 1:
                break
            else:
                heappush(heap, -(largest//2))
        # print(f'{heap}')
        # print(f'{ans}')
        return ans

sol = Solution()
assert sol.minimumDeviation([3,5]) == 1
assert sol.minimumDeviation([1,2,3,4]) == 1
assert sol.minimumDeviation([4,1,5,20,3]) == 3
