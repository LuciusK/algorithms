from functools import lru_cache
class Solution:
    @lru_cache(None)
    def canWin(self, s: str) -> bool:
        n = len(s)
        for i in range(n - 1):
            if s[i] == s[i + 1] == '+':
                if not self.canWin(s[:i] + '--' + s[i + 2:]):
                    return True
        return False