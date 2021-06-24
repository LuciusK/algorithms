class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            n1 = int(num1[i])
            for j in range(n - 1, -1, -1):
                n2 = int(num2[j])
                sm = res[i + j + 1] + n1 * n2
                res[i + j + 1] = sm % 10
                res[i + j] += sm // 10
        idx = 1 if res[0] == 0 else 0
        return ''.join(str(x) for x in res[idx:])