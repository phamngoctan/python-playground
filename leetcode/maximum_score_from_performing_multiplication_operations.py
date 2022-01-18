from typing import List

class Solution:
  def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
    """ Time complexity O(m^2)
    Be aware, assign the leftValue and rightValue in each position causes TLE
    """
    N, M = len(nums), len(multipliers)
    
    def solve(memo, left, i):
      if i >= M: # base case
        return 0
      if not memo[left][i]:
        right = N - 1 - i + left
        mult = multipliers[i]
        memo[left][i] = max(nums[left] * mult + solve(memo, left + 1, i + 1), 
                            nums[right] * mult + solve(memo, left, i + 1))
      return memo[left][i]
    memo = [[None for _ in range(M)] for _ in range(M)]
    ans = solve(memo, 0, 0)
    # print(f'{ans}')
    # print(f'{memo}')
    return ans
  
  def maximumScore_TLE(self, nums: List[int], multipliers: List[int]) -> int:
    """Doesn't need the right because it can be calculated
    Be aware, the memo should be a two dimension array
    """
    N, M = len(nums), len(multipliers)
    
    def solve(memo, left, i):
      if i >= M: # base case
        return 0
      if not memo[left][i]:
        right = N - 1 - i + left
        mult = multipliers[i]
        leftValue = nums[left] * mult + solve(memo, left + 1, i + 1)
        rightValue = nums[right] * mult + solve(memo, left, i + 1)
        memo[left][i] = max(leftValue, rightValue)
      return memo[left][i]
    memo = [[0 for _ in range(M)] for _ in range(M)]
    ans = solve(memo, 0, 0)
    # print(f'{ans}')
    # print(f'{memo}')
    return ans
  
  def maximumScore_TLE(self, nums: List[int], multipliers: List[int]) -> int:
    """Doesn't need the right because it can be calculated
    Be aware, the memo should be a two dimension array
    """
    N, M = len(nums), len(multipliers)
    
    def solve(memo, left, i):
      if i == M: # base case
        return 0
      if not (i, left) in memo:
        right = N - 1 - i + left
        mult = multipliers[i]
        leftValue = nums[left] * mult + solve(memo, left + 1, i + 1)
        rightValue = nums[right] * mult + solve(memo, left, i + 1)
        memo[(i, left)] = max(leftValue, rightValue)
      return memo[(i, left)]
    memo = {}
    ans = solve(memo, 0, 0)
    # print(f'{ans}')
    print(f'{memo}')
    return ans

sol = Solution()
assert sol.maximumScore([1,2,3], multipliers = [3,2,1]) == 14
assert sol.maximumScore([-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]) == 102
