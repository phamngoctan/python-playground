from typing import List

class Solution:
  def countBattleships(self, board: List[List[str]]) -> int:
    R = len(board)
    C = len(board[0])
    def isValid(x, y):
      return x >= 0 and x < R and y >= 0 and y < C
    count = 0
    for i in range(R):
      for j in range(C):
        if board[i][j] == 'X':
          if isValid(i - 1, j) and board[i - 1][j] == 'X':
            continue
          if isValid(i, j - 1) and board[i][j - 1] == 'X':
            continue
          count += 1
    # print(f'{count}')
    return count
sol = Solution()
assert sol.countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]) == 2
assert sol.countBattleships([['.']]) == 0
assert sol.countBattleships([['X']]) == 1
assert sol.countBattleships([["X",".","X"]]) == 2
