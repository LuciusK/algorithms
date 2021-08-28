class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        m = len(mat)
        n = len(mat[0])
        for i in mat:
            i.sort()
        self.res = float('inf')
        
        @lru_cache(None)
        def dfs(cur, cum):
            if cur == m:
                self.res = min(self.res, abs(cum - target))
                return
            
            for i in range(n):
                res = cum + mat[cur][i]
                if res >= target and res - target > self.res:
                    return
                dfs(cur + 1, res)
        
        dfs(0, 0)
        return self.res