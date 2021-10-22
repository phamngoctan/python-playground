class Solution:
  def lengthOfLastWord(self, s: str) -> int:
    count = 0
    for i in range(len(s) - 1, 0 - 1, -1):
      if s[i] != ' ':
        count += 1
      if s[i] == ' ' and count != 0:
        return count
    return count
sol = Solution()
assert sol.lengthOfLastWord("Hello World") == 5
assert sol.lengthOfLastWord("   fly me   to   the moon  ") == 4
assert sol.lengthOfLastWord("luffy is still joyboy") == 6
assert sol.lengthOfLastWord(" n      ") == 1
assert sol.lengthOfLastWord("ab ") == 2
