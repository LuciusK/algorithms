class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n < 4 or n > 12:
            return []
        path = []
        res = []
        split = 0
        begin = 0
        self.dfs(s, n, split, begin, path, res)
        return res
    
    def dfs(self, s, n, split, begin, path, res):
        if begin == n:
            if split == 4:
                res.append('.'.join(path[:]))
            return 
        
        if n - begin < 4 - split and n - begin > 3 * (4 - split):
            return
        
        for i in range(3):
            if begin + i >= n:
                break
            ip = self.ip_judge(s, begin, begin + i)
            if ip != -1:
                path.append(str(ip))
                self.dfs(s, n, split + 1, begin + i + 1, path, res)
                path.pop()

    def ip_judge(self, s, left, right):
        size = right - left + 1
        if size > 1 and s[left] == '0':
            return -1
        res = int(s[left:right + 1])
        if res > 255:
            return -1
        return res