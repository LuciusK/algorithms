class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 如果 A > B ,则按照左规则处理后，B不会比A多；按照右规则处理后，
        # A一定比B多，那么A一定会被更新（变大），但L、R规则仍然成立：B不会比A多，A一定比B多
        n = len(ratings)
        left = [1 for _ in range(n)]
        right = left[:]
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        count = left[-1]
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
            count += max(left[i], right[i])
        return count