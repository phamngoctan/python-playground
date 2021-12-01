from typing import List

class Solution:
  def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
    MAX = len(accounts)
    parent = [i for i in range(MAX)]
    ranks = [0 for _ in range(MAX)]
    def findSet(u):
      while u != parent[u]:
        u = parent[u]
      return u
    def unionSet(u, v):
      uParent = findSet(u)
      vParent = findSet(v)
      if uParent == vParent:
        return
      if ranks[uParent] > ranks[vParent]:
        parent[vParent] = uParent
      elif ranks[uParent] < ranks[vParent]:
        ranks[uParent] = vParent
      else:
        parent[uParent] = vParent
    
    from collections import defaultdict
    hash = defaultdict(list)
    for i, email in enumerate(accounts):
      for email in email[1:]:
        hash[email].append(i)
    # print(f'{hash}')
    
    for nodeIds in hash.values():
      for nodeId in nodeIds[1:]:
        unionSet(nodeId, nodeIds[0]) # set the first nodeId is the parent of all subsequence node
    # print(f'{parent}')
    # union all the nodes [0, 0, 2, 3] 
    # 1 & 0 has the same parent is 0
    # 2, 3 is parent itself
    
    mergedAccounts = defaultdict(set)
    for i, email in enumerate(accounts):
      parentNodeId = findSet(i)
      mergedAccounts[parentNodeId].update(email[1:])
    # print(f'{mergedAccounts}')
    # {0: {'john_newyork@mail.com', 'john00@mail.com', 'johnsmith@mail.com'}, 
    # 2: {'mary@mail.com'}, 
    # 3: {'johnnybravo@mail.com'}}
    
    ans = []
    for i, emails in mergedAccounts.items():
      # tmp = []
      # tmp.append(accounts[i][0])
      # tmp.extend(sorted(list(emails)))
      ans.append([accounts[i][0]] + sorted(list(emails)))
    # print(f'{ans}')
    return ans
    
sol = Solution()
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
            ["John","johnsmith@mail.com","john00@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]]
assert sol.accountsMerge(accounts) == [
            ["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]]

accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
            ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
            ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
            ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
            ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
assert sol.accountsMerge(accounts) == [
                                       ["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
                                       ["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
                                       ["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],
                                       ["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],
                                       ["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]

accounts = [["David","David5@m.co","David8@m.co"],
            ["David","David1@m.co","David1@m.co","David8@m.co"],
            ["David","David0@m.co","David0@m.co","David5@m.co"]]
assert sol.accountsMerge(accounts) == [["David","David0@m.co","David1@m.co","David5@m.co","David8@m.co"]]

