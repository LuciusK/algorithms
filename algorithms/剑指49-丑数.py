class Solution:
    def nthUglyNumber(self, n: int) -> int:
        import heapq
        heap = [1]
        heapq.heapify(heap)
        res = 0
        for _ in range(n):
            res = heapq.heappop(heap)
            while heap and res == heap[0]:
                res = heapq.heappop(heap)
            a, b, c = res * 2, res * 3, res * 5
            for t in [a, b, c]:
                heapq.heappush(heap, t)
        return res

    def nthUglyNumber1(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        p1 = 0
        p2 = 0
        p3 = 0
        for i in range(1, n):
            dp[i] = min(2*dp[p1], 3*dp[p2], 5*dp[p2])
            if dp[i] == 2*dp[p1]:
                p1 += 1
            if dp[i] == 3*dp[p2]:
                p2 += 1
            if dp[i] == 5*dp[p3]:
                p3 += 1
        return dp[-1]