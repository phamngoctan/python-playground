from typing import Annotated, List

class Solution:
  def solve(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    R = len(board)
    C = len(board[0])
    direction = [[0,1],[0,-1],[1,0],[-1,0]]
    def isValid(x, y):
      return x >= 0 and x < R and y >= 0 and y < C
    def dfs(grid, pos):
      x, y = pos
      grid[x][y] = 'T'
      for dir in direction:
        newX = x + dir[0]
        newY = y + dir[1]
        if not isValid(newX, newY) or grid[newX][newY] != 'O':
          continue
        dfs(grid, [newX, newY])
    for i in range(R):
      for j in range(C):
        if (i == 0 or i == R - 1 or j == 0 or j == C - 1) and board[i][j] == 'O':
          dfs(board, [i, j])

    for i in range(R):
      for j in range(C):
        if board[i][j] == 'O':
          board[i][j] = 'X'
        elif board[i][j] == 'T':
          board[i][j] = 'O'
    # print(f'{board}')
sol = Solution()
input = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
sol.solve(input)
assert input == [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

input = [["X"]]
sol.solve(input)
assert input == [["X"]]