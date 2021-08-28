class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        res = []
        def dfs(cur, x):
            if len(cur) == n:
                res.append(int(cur, 2))
                return 

            if x == 0:
                # 00, 01
                dfs(cur + '0', 0)
                dfs(cur + '1', 1)
            else:
                # 11, 10
                dfs(cur + '1', 0)
                dfs(cur + '0', 1)
        
        dfs('', 0)
        return res