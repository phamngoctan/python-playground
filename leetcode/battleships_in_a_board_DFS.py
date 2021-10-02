from typing import List

class Solution:
  def countBattleships(self, board: List[List[str]]) -> int:
    R = len(board)
    C = len(board[0])
    def isValid(x, y):
      return x < R and y < C
    def dfs(board, pos):
      board[pos[0]][pos[1]] = '.'
      newX = pos[0] + 1
      newY = pos[1] + 1
      if isValid(pos[0], newY) and board[pos[0]][newY] == 'X':
        dfs(board, [pos[0], newY])
      if isValid(newX, pos[1]) and board[newX][pos[1]] == 'X':
        dfs(board, [newX, pos[1]])
    count = 0
    for i in range(R):
      for j in range(C):
        if board[i][j] == 'X':
          dfs(board, [i, j])
          count += 1
    # print(f'{count}')
    return count
sol = Solution()
assert sol.countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]) == 2
assert sol.countBattleships([['.']]) == 0
assert sol.countBattleships([['X']]) == 1