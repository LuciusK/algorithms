class Solution:
    def countAndSay(self, n: int) -> str:
        pre = ''
        cur = '1'
        for i in range(1, n):
            pre = cur
            cur = ''
            start = 0
            end = 0
            while end < len(pre):
                while end < len(pre) and pre[end] == pre[start]:
                    end += 1
                cur += str(end - start) + pre[start]
                start = end
        return cur