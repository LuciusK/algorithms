#
# @lc app=leetcode id=1411 lang=python3
#
# [1411] Number of Ways to Paint N × 3 Grid
#

# @lc code=start
class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10 ** 9 + 7
        types = list()
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if i != j and j != k:
                        types.append(i * 9 + j * 3 + k)
        type_cnt = len(types)
        related = [[0] * type_cnt for _ in range(type_cnt)]
        for i, ti in enumerate(types):
            x1, x2, x3 = ti // 9, ti // 3 % 3, ti % 3
            for j, tj in enumerate(types):
                y1, y2, y3 = tj // 9, tj // 3 % 3, tj % 3
                if x1 != y1 and x2 != y2 and x3 != y3:
                    related[i][j] = 1
        f = [[0] * type_cnt for _ in range(n + 1)]
        f[1] = [1] * type_cnt
        for i in range(2, n + 1):
            for j in range(type_cnt):
                for k in range(type_cnt):
                    if related[j][k]:
                        f[i][j] += f[i - 1][k]
                        f[i][j] %= mod
        ans = sum(f[n]) % mod
        return ans

    def numOfWays1(self, n: int) -> int:
        mod = 10 ** 9 + 7
        fi0, fi1 = 6, 6
        for i in range(2, n + 1):
            fi0, fi1 = (2 * fi0 + 2 * fi1) * mod, (2 * fi0 + 3 * fi1) % mod
        return (fi0 + fi1) % mod
        
# @lc code=end

