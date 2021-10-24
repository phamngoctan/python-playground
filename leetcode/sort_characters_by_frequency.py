class Solution:
  def frequencySort(self, s: str) -> str:
    freq = {}
    for sub in s:
      if not sub in freq:
        freq[sub] = 0
      freq[sub] += 1
    # print(f'{freq}')
    buckets = [[] for _ in range(len(s) + 1)]
    for key, val in freq.items():
      buckets[val].append(key)
    strRes = ""
    for i in range(len(buckets) - 1, 0, -1):
      for j in range(len(buckets[i])):
        for k in range(i):
          strRes += buckets[i][j]
    # print(f'{strRes}')
    return strRes

sol = Solution()
assert sol.frequencySort("tree") == "eetr"
assert sol.frequencySort("cccaaa") == "cccaaa"
assert sol.frequencySort("Aabb") == "bbAa"
assert sol.frequencySort("aA") == "aA"
assert sol.frequencySort("a") == "a"
