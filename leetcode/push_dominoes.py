class Solution(object):
    def pushDominoes(self, dominoes: str) -> str:
        forces = [0 for _ in range(len(dominoes))]
        MAX_FORCE = len(dominoes)
        
        force = 0
        for i, val in enumerate(dominoes):
            if val == "R":
                force = MAX_FORCE
            elif val == "L":
                force = 0
            else:
                force = max(0, force - 1)
            forces[i] = force
        # print(f"{forces}")
        for i in range(len(dominoes) -1, -1, -1):
            val = dominoes[i]
            if val == "L":
                force = MAX_FORCE
            elif val == "R":
                force = 0
            else:
                force = max(0, force - 1)
            forces[i] -= force
        # print(f"{forces}")
        ans = ""
        for force in forces:
            if force > 0:
                ans += "R"
            elif force < 0:
                ans += "L"
            else:
                ans += "."
        return ans

# print(Solution().pushDominoes("RR.L"))
assert Solution().pushDominoes("RR.L") == "RR.L"
# print(Solution().pushDominoes(".L.R...LR..L.."))
assert Solution().pushDominoes(".L.R...LR..L..") == "LL.RR.LLRRLL.."
# print(Solution().pushDominoes("..R...L..R."))
assert Solution().pushDominoes("..R...L..R.") == "..RR.LL..RR"
print(f"Finish the assertion check without any error")
