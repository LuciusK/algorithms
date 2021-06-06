class Solution:
    def spiralOrder(self, matrix:[[int]]) -> [int]:
        if not matrix:
            return []
        l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            t += 1
            if t > b:
                break
            for i in range(t, b + 1):
                res.append(matrix[i][r])
            r -= 1
            if l > r:
                break
            for i in range(r, l - 1, -1):
                res.append(matrix[b][i])
            b -= 1
            if t > b:
                break
            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r:
                break
        return res
    
    def spiralOrder1(self, matrix:[[int]]) -> [int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res