from typing import List

class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
    R = len(board)
    C = len(board[0])
    direction = [[0,1],[0,-1],[1,0],[-1,0]]
    # visited = [[False for i in range(C)] for j in range(R)]
    # print(f'{board}')
    def isNotValid(x, y):
      return x < 0 or y < 0 or x >= R or y >= C
    def dfs(pos, level):
      visited[pos[0]][pos[1]] = True
      for i in range(4):
        newX = pos[0] + direction[i][0]
        newY = pos[1] + direction[i][1]
        if isNotValid(newX, newY) or visited[newX][newY]:
          continue
        # print(f'{newX},{newY}: {board[newX][newY]} vs {word[level + 1]} {level + 1}')
        if board[newX][newY] == word[level + 1]:
          if len(word) - 1 == level + 1:
            return True
          if dfs([newX, newY], level + 1):
            return True
      visited[pos[0]][pos[1]] = False
      return False
      
    for i in range(R):
      for j in range(C):
        if board[i][j] == word[0]:
          if len(word) == 1:
            return True
          visited = [[False for i in range(C)] for j in range(R)]
          # print(f'{visited}')
          # print(f'{i}, {j}')
          # if i == 1 and j == 1:
            # print(f'Hey')
          if dfs([i,j], 0):
            return True
    return False
    
sol = Solution()
assert sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED") == True
assert sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE") == True
assert sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB") == False
assert sol.exist([["A"]], word = "ABCB") == False
assert sol.exist([["A","B","C","E"]], word = "ABCE") == True
assert sol.exist([["A","B","C","E"]], word = "AE") == False
assert sol.exist([["A"],["S"],["A"]], word = "ASA") == True
assert sol.exist([["A"],["S"],["A"]], word = "A") == True
assert sol.exist([["A"],["S"],["A"]], word = "AS") == True
assert sol.exist([["C","A","A"],["A","A","A"],["B","C","D"]], word = "AAB") == True
