class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        p1, p2 = 0, 0
        end = max(len(version1), len(version2))
        while p1 < end or p2 < end:
            v1, v2 = 0, 0
            while p1 < len(version1) and version1[p1] != '.':
                v1 = v1 * 10 + int(version1[p1])
                p1 += 1
            while p2 < len(version2) and version2[p2] != '.':
                v2 = v2 * 10 + int(version2[p2])
                p2 += 1
            if v1 > v2:
                return 1
            elif v2 > v1 :
                return -1
            p1 += 1
            p2 += 1
        return 0