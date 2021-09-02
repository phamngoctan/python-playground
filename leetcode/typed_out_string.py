class Solution:
  def backspaceCompare(self, s: str, t: str) -> bool:      
    p1 = len(s) - 1
    p2 = len(t) - 1
    while p1 >= 0 or p2 >= 0:
      if (p1 >= 0 and s[p1] == '#') or (p2 >= 0 and t[p2] == '#'):
        if p1 >= 0 and s[p1] == '#':
          countBack = 2
          while countBack > 0:
            countBack -= 1
            p1 -= 1
            if p1 > 0 and s[p1] == '#':
              countBack += 2

        if p2 >= 0 and t[p2] == '#':
          countBack = 2
          while countBack > 0:
            countBack -= 1
            p2 -= 1
            if p2 > 0 and t[p2] == '#':
              countBack += 2
              
      else:
        # print(f'{p1} - {p2}')
        if (p1 >= 0 and p2 < 0) or (p1 < 0 and p2 >= 0) or (s[p1] != t[p2]) :
          return False
        else:
          p1 -= 1
          p2 -= 1
    return True

sol = Solution()
assert sol.backspaceCompare('abc#d', 'abz#d') == True
assert sol.backspaceCompare('abc#d', 'abzaa###d') == True
assert sol.backspaceCompare('a##c', '#a#c') == True
assert sol.backspaceCompare('a#c', 'b') == False
assert sol.backspaceCompare('r', '#') == False
assert sol.backspaceCompare('#', 'r') == False
assert sol.backspaceCompare('#', '####') == True
