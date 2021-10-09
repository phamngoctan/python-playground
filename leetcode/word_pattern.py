class Solution:
  def wordPattern(self, pattern: str, s: str) -> bool:
    arr = s.split(' ')
    if len(arr) != len(pattern):
      return False
    
    freq = {}
    for i, value in enumerate(arr):
      if not value in freq:
        if pattern[i] in freq.values():
          return False
        freq[value] = pattern[i]
      elif freq[value] != pattern[i]:
        return False
    return True
  
  def wordPattern_v1(self, pattern: str, s: str) -> bool:
    arr = s.split(' ')
    print(f'{arr}')
    sPattern = []
    freq = {}
    next = 96
    for i in range(len(arr)):
        if not arr[i] in freq:
            freq[arr[i]] = chr(next + 1)
            next += 1
        sPattern.append(freq[arr[i]])
    # print(f'{freq}')
    # print(f'{sPattern}')
    arr2 = pattern
    sPattern2 = []
    freq = {}
    next = 96
    for i in range(len(arr2)):
      if not arr2[i] in freq:
        freq[arr2[i]] = chr(next + 1)
        next += 1
      sPattern2.append(freq[arr2[i]])
    # print(f'{freq}')
    # print(f'{sPattern}')
    return ''.join(sPattern) == ''.join(sPattern2)
sol = Solution()
assert sol.wordPattern("abba", "dog cat cat dog") == True
assert sol.wordPattern("cccc", "dog dog dog dog") == True
assert sol.wordPattern("aaaa", "dog cat cat dog") == False
assert sol.wordPattern("abba", "dog cat cat fish") == False
