class Solution:
  def largestOddNumber(self, num: str) -> str:
    for i in range(len(num) - 1, 0 - 1, -1):
      if int(num[i]) % 2 == 1:
        return num[:i + 1]
    return ""

sol = Solution()
assert sol.largestOddNumber("52") == "5"
assert sol.largestOddNumber("4206") == ""
assert sol.largestOddNumber("35427") == "35427"
assert sol.largestOddNumber("52") == "5"
assert sol.largestOddNumber("10222134") == "1022213"
assert sol.largestOddNumber("3323222") == "3323"
assert sol.largestOddNumber("2") == ""
assert sol.largestOddNumber("5") == "5"
