from typing import List

class Solution:
  def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    '''
    Should try with BFS/DFS approach to get more idea
    '''
    parent = {}
    vals = {}
    # def findSet2(u):
    #   while u != parent.setdefault(u, u):
    #     pp = parent[u]
    #     vals[u] = vals.get(u) * vals.get(pp)
    #     parent[u] = pp
    #     u = pp
    #   return u
    def findSet(u):
      vals.setdefault(u, 1.0)
      p = parent.setdefault(u, u)
      if u != p:
        pp = findSet(p)
        vals[u] = vals.get(u) * vals.get(p)
        parent[u] = pp
      return parent[u]
    def unionSet(u, v, inputVal):
      uParent = findSet(u)
      vParent = findSet(v)
      if uParent == vParent:
        return
      parent[uParent] = vParent
      vals[uParent] = inputVal * vals[v]/vals[u]
    
    for index, equation in enumerate(equations):
      a, b = equation
      unionSet(a, b, values[index])
    ans = []
    for x,y in queries:
      evaluatedVal = -1
      if x in parent and y in parent and findSet(x) == findSet(y):
        evaluatedVal = vals[x]/vals[y]
      ans.append(evaluatedVal)
    print(f'{ans}')
    return ans

sol = Solution()
assert sol.calcEquation( 
               [["a","b"],["b","c"]], 
               values = [2.0,3.0], 
               queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]) == [6.00000,0.50000,-1.00000,1.00000,-1.00000]
assert sol.calcEquation( 
               [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]],
               values = [3.0,4.0,5.0,6.0],
               queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]) == [360.0, 0.008333333333333333, 20.0, 1.0, -1, -1]
