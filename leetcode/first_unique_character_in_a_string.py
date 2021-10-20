class Solution:
  def firstUniqChar(self, s: str) -> int:
    freq = {}
    for i in s:
      if not i in freq:
        freq[i] = 0
      freq[i] += 1
    for index, val in enumerate(s):
      if freq[val] == 1:
        return index
    return -1
sol = Solution()
assert sol.firstUniqChar("leetcode") == 0
assert sol.firstUniqChar("loveleetcode") == 2
assert sol.firstUniqChar("aabb") == -1
assert sol.firstUniqChar("a") == 0
