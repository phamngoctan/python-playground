from typing import List
from queue import Queue

class Solution:
  def minMutation(self, start: str, end: str, bank: List[str]) -> int:
    bank = set(bank)
    queue = Queue()
    queue.put(start)
    count = 1
    while queue.qsize() > 0:
      queueLength = queue.qsize()
      for _ in range(queueLength):
        cur = queue.get()
        # print(f'{cur}')
        for i in range(8):
          for j in "ACGT":
            newChar = cur[:i] + j + cur[i + 1:]
            # print(f'{newChar}')
            if newChar in bank:
              bank.remove(newChar)
              queue.put(newChar)
              if newChar == end:
                return count
      count += 1
    return -1
sol = Solution()
assert sol.minMutation("AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]) == 1
assert sol.minMutation("AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]) == 2
assert sol.minMutation("AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]) == 3
assert sol.minMutation("AAAAACCC", end = "AACCCACA", bank = ["AAAACCCC","AAACCCCC","AACCCACA"]) == -1
assert sol.minMutation("AAAAACCC", end = "AACCCCCA", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]) == -1
