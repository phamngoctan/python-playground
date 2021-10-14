from typing import List

class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    def isValid(row, col, box, val):
      return not row[val] and not col[val] and not box[val]
    def getBoxId(r, c):
      rowPos = c // 3
      colPos = (r // 3) * 3
      return rowPos + colPos
    rows = [[False for i in range(10)] for j in range(9)]
    cols = [[False for i in range(10)] for j in range(9)]
    boxes = [[False for i in range(10)] for j in range(9)]
    for r in range(9):
      for c in range(9):
        if board[r][c] != '.':
          row = rows[r]
          col = cols[c]
          box = boxes[getBoxId(r, c)]
          val = int(board[r][c])
          if isValid(row, col, box, val):
            row[val] = True
            col[val] = True
            box[val] = True
          else:
            return False
    return True

sol = Solution()
assert sol.isValidSudoku(
  [
     ["5","3",".", ".","7",".", ".",".","."]
    ,["6",".",".", "1","9","5", ".",".","."]
    ,[".","9","8", ".",".",".", ".","6","."]

    ,["8",".",".", ".","6",".", ".",".","3"]
    ,["4",".",".", "8",".","3", ".",".","1"]
    ,["7",".",".", ".","2",".", ".",".","6"]

    ,[".","6",".", ".",".",".", "2","8","."]
    ,[".",".",".", "4","1","9", ".",".","5"]
    ,[".",".",".", ".","8",".", ".","7","9"]
  ]) == True

assert sol.isValidSudoku(
  [
     ["8","3",".", ".","7",".", ".",".","."]
    ,["6",".",".", "1","9","5", ".",".","."]
    ,[".","9","8", ".",".",".", ".","6","."]

    ,["8",".",".", ".","6",".", ".",".","3"]
    ,["4",".",".", "8",".","3", ".",".","1"]
    ,["7",".",".", ".","2",".", ".",".","6"]

    ,[".","6",".", ".",".",".", "2","8","."]
    ,[".",".",".", "4","1","9", ".",".","5"]
    ,[".",".",".", ".","8",".", ".","7","9"]]) == False
