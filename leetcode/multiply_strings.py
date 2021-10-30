class Solution:
  def multiply(self, num1: str, num2: str) -> str:
    arrRes = [0 for i in range(len(num1) + len(num2))]
    position = len(arrRes) - 1
    for n1 in reversed(num1):
      tmpPos = position
      for n2 in reversed(num2):
        arrRes[tmpPos] += int(n1) * int(n2)
        arrRes[tmpPos - 1] += arrRes[tmpPos] // 10
        arrRes[tmpPos] = arrRes[tmpPos] % 10
        tmpPos -= 1
      position -= 1
    point = 0
    while point < len(arrRes) - 1 and arrRes[point] == 0:
      point += 1
    # print(f'{arrRes}')
    # print(f'{arrRes[point:]}')
    return ''.join(map(str, arrRes[point:]))
sol = Solution()
assert sol.multiply("123", "456") == "56088"
