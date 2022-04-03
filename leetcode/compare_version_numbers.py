class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        # print(f'{v1} {v2}')
        if len(v1) != len(v2):
            if len(v1) > len(v2):
                while len(v2) < len(v1):
                    v2.append("0")
            else:
                while len(v1) < len(v2):
                    v1.append("0")
        for i in range(len(v1)):
            curV1 = v1[i].lstrip("0")
            curV1 = int(curV1) if curV1 else 0
            curV2 = v2[i].lstrip("0")
            curV2 = int(curV2) if curV2 else 0
            # print(f'{curV1} {curV2}')
            if curV1 > curV2:
                return 1
            elif curV1 < curV2:
                return -1
        return 0

sol = Solution()
assert sol.compareVersion("1.01", "1.001") == 0
assert sol.compareVersion("1.01", "1.01.00") == 0
assert sol.compareVersion("1.011", "1.01.00") == 1
assert sol.compareVersion("1.01", "1.1.01") == -1
