class Solution:
  """GGLLGG means origin: 0,0 to 0,1 0,2 next turn L (left) two times -> 180 degrees
  -> turn direction back to the root (LL) -> GG means move two times back to root (0,0)
  -> Circle
  # GLL -> start is ^ -> move one up -> LL ( from ^ to Left one time 
  # -> and one more Left mean goes Down)
  """
  def isRobotBounded(self, instructions: str) -> bool:
    cur = [0,0]
    dirs = [[1,0], [0,1], [-1,0], [0,-1]]
    dir = 0; # 0:north(up), 1: right, 2: down, 3: left
    for val in instructions:
      if val == 'G':
        cur[0] += dirs[dir][0]
        cur[1] += dirs[dir][1]
      elif val == 'L':
        dir = (dir + 3) % 4
      else:
        dir = (dir + 1) % 4
    # print(f'{cur}')
    if cur == [0,0]:
      return True
    if dir == 0 and cur != [0,0]:
      return False
    return True

sol = Solution()
assert sol.isRobotBounded("GGLLGG") == True
assert sol.isRobotBounded("GG") == False
assert sol.isRobotBounded("GL") == True
