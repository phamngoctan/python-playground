class Solution:
  def fib(self, n: int) -> int:
    arr = [0, 1]
    for i in range(2, n + 1):
      arr.append(arr[i - 2] + arr[i - 1])
    return arr[n]

sol = Solution()
assert sol.fib(3) == 2
assert sol.fib(4) == 3
assert sol.fib(5) == 5
assert sol.fib(30) == 832040