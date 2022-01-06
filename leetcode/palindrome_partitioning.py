from typing import List

class Solution:
  """[Notice]
  1 <= s.length <= 16
  the constraint is quite clear that there will be no O(n) or nlog(n) here :)
  """
  def partition(self, s: str) -> List[List[str]]:
    '''
    Borrow idea from LC
    '''
    ans = []
    if not s: return ans
    self.dfs(0, s, [], ans)
    # print(f'{ans}')
    return ans

  def dfs(self, index, s, path, ans):
    if index == len(s):
      # ans.append(path)
      # without the deep copy, the result will be [[]]
      ans.append(path[::])
      return
    for i in range(index, len(s)):
      #// only do backtracking when current string is palindrome
      if not self.isPalindrome(s, index, i): continue
      indexToCurIDistance = index + (i - index + 1)
      path.append(s[index:indexToCurIDistance])
      self.dfs(i + 1, s, path, ans)
      path.pop()
    
  def isPalindrome(self, s, l, r):
    while l < r:
      if s[l] != s[r]:
        return False
      l += 1
      r -= 1
    return True

sol = Solution()
assert sol.partition("aab") == [["a","a","b"],["aa","b"]]
assert sol.partition("a") == [["a"]]
