class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        n2 = len(s2)
        if n != n2:
            return False
        dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dp[i][j][1] = s1[i] == s2[j]
        for k in range(2, n + 1):
            for i in range(n - k + 1):
                for j in range(n - k + 1):
                    for w in range(1, k):
                        if dp[i][j][w] and dp[i + w][j + w][k - w]:
                            dp[i][j][k] = True
                        if dp[i][j + k - w][w] and dp[i + w][j][k - w]:
                            dp[i][j][k] = True
        return dp[0][0][n]