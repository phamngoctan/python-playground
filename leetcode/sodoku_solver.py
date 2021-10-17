from typing import List

class Solution:
  def solveSudoku(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    rows = [[False for i in range(10)] for j in range(9)]
    # rows[0][9] = True
    # print(f'{rows[0][0]}')
    # print(f'{rows}')
    cols = [[False for i in range(10)] for j in range(9)]
    boxes = [[False for i in range(10)] for j in range(9)]
    def getBoxId(r, c):
      valFromCol = c // 3
      valFromRow = (r // 3) * 3
      return valFromCol + valFromRow
    # print(f'value {getBoxId(7, 6)} must equal 8')
    for i in range(9):
      for j in range(9):
        if board[i][j] != '.':
          valInBoard = int(board[i][j])
          rows[i][valInBoard] = True
          cols[j][valInBoard] = True
          boxes[getBoxId(i, j)][valInBoard] = True
    # print(f'rows: {rows}')
    # print(f'-----------------')
    # print(f'cols: {cols}')
    # print(f'-----------------')
    # print(f'boxes: {boxes}')
    def isValid(box, row, col, val):
      return not row[val] and not col[val] and not box[val]
    def solveBacktracking(board, boxes, rows, cols, r, c):
      if r == 9 or c == 9:
        return True
      else:
        if board[r][c] == '.':
          for num in range(1, 10):
            numVal = str(num)
            board[r][c] = numVal
            box = boxes[getBoxId(r, c)]
            row = rows[r]
            col = cols[c]
            if isValid(row, col, box, num):
              row[num] = True
              col[num] = True
              box[num] = True
              if c == 8:
                if solveBacktracking(board, boxes, rows, cols, r + 1, 0):
                  return True
              else:
                if solveBacktracking(board, boxes, rows, cols, r, c + 1):
                  return True
              row[num] = False
              col[num] = False
              box[num] = False
            board[r][c] = '.'
        else:
          if c == 8:
            if solveBacktracking(board, boxes, rows, cols, r + 1, 0):
              return True
          else:
            if solveBacktracking(board, boxes, rows, cols, r, c + 1):
              return True
    solveBacktracking(board, boxes, rows, cols, 0, 0)
    return board

sol = Solution()
assert sol.solveSudoku(
  [
    ["5","3",".", ".","7",".", ".",".","."],
    ["6",".",".", "1","9","5", ".",".","."],
    [".","9","8", ".",".",".", ".","6","."],

    ["8",".",".", ".","6",".", ".",".","3"],
    ["4",".",".", "8",".","3", ".",".","1"],
    ["7",".",".", ".","2",".", ".",".","6"],
    
    [".","6",".", ".",".",".", "2","8","."],
    [".",".",".", "4","1","9", ".",".","5"],
    [".",".",".", ".","8",".", ".","7","9"]
  ]) == [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]]
