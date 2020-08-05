#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur_str = ''

        def dfs(cur_str, left, right):
            if left == 0 and right == 0:# equals to n is ok
                res.append(cur_str)
                return
            if right < left:
                return
            if left > 0:
                dfs(cur_str + '(', left - 1, right)# if we used n, then left need to add 1
            if right > 0:
                dfs(cur_str + ')', left, right - 1)# same as right

        dfs(cur_str, n, n)
        return res

    def generateParenthesis1(self, n: int) -> List[str]:
        if n == 0:
            return []
        
        dp = [False for _ in range(n+1)]
        dp[0] = [""]

        for i in range(1, n + 1):
            cur = []
            for j in range(i):
                left = dp[j]
                right = dp[i-j-1]
                for s1 in left:
                    for s2 in right:
                        cur.append("(" + s1 + ")" + s2)
            dp[i] = cur
        return dp[n]


# @lc code=end

