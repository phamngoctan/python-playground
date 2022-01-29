import math

class Solution:
  def winnerSquareGame_notYet(self, n: int) -> bool:
    """ TODO: come back to this approach later, 
    not yet figure out how to use only one dimensional array
    """
    def dp(n, isAliceTurn, memo):
      if n == 0: # base case, the last turn that this player lose the game
        if isAliceTurn:
          return False
        else:
          return True
      
      if memo[n] == None:
        # print(f'Hey {int(math.sqrt(n))}')
        ans = False
        for i in range(1, int(math.sqrt(n)) + 1): # 1, 2 (n = 4), 3 (n = 9) 
          ans = dp(n - i * i, not isAliceTurn, memo)
          if isAliceTurn:
            if ans:
              break
          else:
            if not ans:
              break
        memo[n] = ans
      return memo[n]
    
    memo = [None for _ in range(n + 1)]
    ans = dp(n, True, memo)
    print(f'{memo}')
    # print(f'{ans}')
    return ans
  
  def winnerSquareGame(self, n: int) -> bool:
    def dp(n, isAliceTurn, memo):
      if n == 0: # base case, the last turn that this player lose the game
        if isAliceTurn:
          return False
        else:
          return True
      
      if isAliceTurn:
        if memo[n][1] != None:
          return memo[n][1] == True # Alice answer
      else:
        if memo[n][0] != None:
          return memo[n][0] == True # Bob answer
      # print(f'Hey {int(math.sqrt(n))}')
      ans = False
      for i in range(1, int(math.sqrt(n)) + 1)[::-1]: # 1, 2 (n = 4), 3 (n = 9) 
        ans = dp(n - i * i, not isAliceTurn, memo)
        if isAliceTurn:
          if ans:
            break
        else:
          if not ans:
            break
      if isAliceTurn:
        memo[n][1] = ans
      else:
        memo[n][0] = ans
      return ans
    
    memo = [[None,None] for _ in range(n + 1)]
    ans = dp(n, True, memo)
    print(f'{memo}')
    # print(f'{ans}')
    return ans
    
sol = Solution()
assert sol.winnerSquareGame(1) == True
assert sol.winnerSquareGame(2) == False
assert sol.winnerSquareGame(3) == True
assert sol.winnerSquareGame(4) == True
assert sol.winnerSquareGame(5) == False
assert sol.winnerSquareGame(7) == False
assert sol.winnerSquareGame(8) == True
assert sol.winnerSquareGame(9) == True
# assert sol.winnerSquareGame(74497) == False
