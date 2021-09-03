class Solution:
  def isPalindrome(self, s: str) -> bool:
    ss = ''.join(filter(lambda x : x.isalnum(), s)).lower()
    # print(f'{ss}')
    l, r = 0, len(ss) - 1
    while l < r:
      if ss[l] != ss[r]:
        return False
      l += 1
      r -= 1
    return True

sol = Solution()
assert sol.isPalindrome('alphanumeric  @123__') == False
assert sol.isPalindrome(' ') == True
assert sol.isPalindrome('     ') == True
assert sol.isPalindrome('aba') == True
assert sol.isPalindrome('race car') == True
assert sol.isPalindrome('race a car') == False
assert sol.isPalindrome('A man, a plan, a canal: Panama') == True
