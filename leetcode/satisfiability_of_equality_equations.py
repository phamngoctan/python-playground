from typing import Dict, List

class Solution:
  def equationsPossible(self, equations: List[str]) -> bool:
    '''
    Using DFS can also solve this problem
    '''
    parent = {}
    def findSet(u):
      parent.setdefault(u, u)
      if u != parent[u]:
        u = findSet(parent[u])
      return u
    for equation in equations:
      u, v = None, None
      if "==" in equation:
        u, v = equation.split("==")
        uParent = findSet(u)
        vParent = findSet(v)
        if uParent != vParent:
          parent[uParent] = vParent
    for equation in equations:
      if "!=" in equation:
        u, v = equation.split("!=")
        uParent = findSet(u)
        vParent = findSet(v)
        if uParent == vParent:
          return False
    return True
      
      
sol = Solution()
assert sol.equationsPossible(["a==b","b!=a"]) == False
assert sol.equationsPossible(["a==b","c!=a","b==c"]) == False
assert sol.equationsPossible(["b==a","a==b"]) == True
assert sol.equationsPossible(["b!=b"]) == False
assert sol.equationsPossible(["a==b","b==c","a==c"]) == True
assert sol.equationsPossible(["a==b","b!=c","c==a"]) == False
assert sol.equationsPossible(["c==c","b==d","x!=z"]) == True
