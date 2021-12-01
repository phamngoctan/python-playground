from typing import List

class Solution:
  def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
    hash = {}
    for nodeId, account in enumerate(accounts):
      for j in range(1, len(account)):
        email = account[j]
        if email not in hash:
          hash[email] = set()
        hash[email].add(nodeId)
    # print(f'{hash}')
    
    def dfs(nodeId, allAccountEmails):
      visisted[nodeId] = True
      emails = accounts[nodeId][1:]
      for email in emails:
        allAccountEmails.add(email)
        linkedNodeIds = hash[email]
        for linkedNodeId in linkedNodeIds:
          if not visisted[linkedNodeId]:
            dfs(linkedNodeId, allAccountEmails)
    
    visisted = [False for _ in range(len(accounts))]
    ans = []
    for nodeId, account in enumerate(accounts):
      if not visisted[nodeId]:
        allAccountEmails = set()
        dfs(nodeId, allAccountEmails)
        # curAccountEmails = []
        # curAccountEmails.append(account[0])
        # curAccountEmails.extend(sorted(list(allAccountEmails)))
        # ans.append(curAccountEmails)
        ans.append([account[0]] + sorted(allAccountEmails))
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

