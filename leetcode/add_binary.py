class Solution:
  def addBinary(self, a: str, b: str) -> str:
    res = [0 for _ in range(max(len(a), len(b)) + 1)]
    a = a[::-1]
    b = b[::-1]
    position = len(res) - 1
    for i in range(len(res)):
      res[position] += int(a[i] if i < len(a) else 0) + int(b[i] if i < len(b) else 0)
      res[position - 1] += res[position] // 2
      res[position] = res[position] % 2
      position -= 1
    # print(f'{res}')
    if res[0] == 1:
      return ''.join(str(x) for x in res)
    return ''.join(str(x) for x in res[1:])
sol = Solution()
assert sol.addBinary(a = "11", b = "1") == "100"
assert sol.addBinary(a = "10", b = "1") == "11"
assert sol.addBinary(a = "1010", b = "1011") == "10101"
