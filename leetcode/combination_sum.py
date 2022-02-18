from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(ans, paths, candidates, remain, start):
            if remain < 0:
                return
            if remain == 0:
                ans.append(paths[::])
            else:
                for i in range(start, len(candidates)):
                    paths.append(candidates[i])
                    backtrack(ans, paths, candidates, remain - candidates[i], i)
                    del paths[-1]
        ans = []
        # candidates.sort()
        backtrack(ans, [], candidates, target, 0)
        print(f'{ans}')
        return ans
        
sol = Solution()
assert sol.combinationSum([2,3,6,7], target = 7) == [[2,2,3],[7]]
# assert sol.combinationSum([2,2,3], target = 5) == [[2,3]]
