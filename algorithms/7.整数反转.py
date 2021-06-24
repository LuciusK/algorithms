class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        x1 = abs(x)
        v = (2 ** 31 - 1) // 10
        s = (2 ** 31 - 1) % 10
        while x1 != 0:
            tmp = x1 % 10
            if x > 0 and (res > v or (res == v and tmp > s)):
                return 0
            if x < 0 and (res > v or (res == v and tmp > s + 1)):
                return 0
            res = res * 10 + tmp
            x1 //= 10
        return res if x > 0 else -res