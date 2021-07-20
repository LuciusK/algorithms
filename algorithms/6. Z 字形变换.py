class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s 
        res = ['' for _ in range(numRows)]
        i, d = 0, -1
        for c in s:
            res[i] += c 
            if i == 0 or i == numRows - 1:
                d = -d 
            i += d 
        return ''.join(res)