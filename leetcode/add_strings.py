class Solution:
  def addStrings(self, num1: str, num2: str) -> str:
    res = [0 for i in range(max(len(num1), len(num2)) + 1)]
    position = len(res) - 1
    num1 = num1[::-1]
    num2 = num2[::-1]
    for i in range(len(res)):
      iAtNum1 = num1[i] if i < len(num1) else 0
      iAtNum2 = num2[i] if i < len(num2) else 0
      res[position] += int(iAtNum1) + int(iAtNum2)
      res[position - 1] += res[position] // 10
      res[position] = res[position] % 10
      position -= 1
    # print(f'{position}')
    # print(f'{res}')
    if res[0]:
      return ''.join(str(x) for x in res)
    return ''.join(str(x) for x in res[1:])
sol = Solution()
assert sol.addStrings(num1 = "11", num2 = "123") == "134"
assert sol.addStrings(num1 = "456", num2 = "77") == "533"
assert sol.addStrings(num1 = "0", num2 = "0") == "0"
assert sol.addStrings(num1 = "999", num2 = "999") == "1998"
