class Solution:
  def areNumbersAscending(self, s: str) -> bool:
    arr = s.split(' ')
    lastNumber = -1
    for i in arr:
      if i.isnumeric():
        if int(i) <= lastNumber:
          return False
        lastNumber = int(i)
    return True

sol = Solution()
assert sol.areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles") == True
assert sol.areNumbersAscending("hello world 5 x 5") == False
assert sol.areNumbersAscending("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s") == False
assert sol.areNumbersAscending("4 5 11 26") == True
assert sol.areNumbersAscending("3 2 1") == False
