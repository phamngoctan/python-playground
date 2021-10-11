class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    def encode(s):
        d = {}
        encoded = []
        for c in s:
            if c not in d:
                d[c] = len(d)
            encoded.append(d[c])
        return str(encoded)
    return encode(s) == encode(t)


def groupIsomorphic(strs):
    def encode(s):
        d = {}
        encoded = []
        for c in s:
            if c not in d:
                d[c] = len(d)
            encoded.append(d[c])
        return str(encoded)

    groups = {}
    for s in strs:
        encoded = encode(s)
        if encoded not in groups:
            groups[encoded] = []
        groups[encoded].append(s)

    return list(groups.values())

print(groupIsomorphic(['aab', 'xxy', 'xyz', 'abc', 'def', 'xyx']))
sol = Solution()
assert sol.isIsomorphic(s = "egg", t = "add")  == True
assert sol.isIsomorphic(s = "foo", t = "bar")  == False