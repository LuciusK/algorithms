#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s
        dp = [[False for _ in range(size)] for _ in range(size)]
        max_len = 1
        start = 0
        for i in range(size):
            dp[i][i] = True
        
        for j in range(1, size):
            for i in range(0, j):
                dp[i][j] = (s[i] == s[j]) and (j - i < 3 or dp[i + 1][j - 1])
                # if s[i] == s[j]:
                #     if j - i < 3:
                #         dp[i][j] = True
                #     else:
                #         dp[i][j] = dp[i + 1][j - 1]
                # else:
                #     dp[i][j] = False
                if dp[i][j] and j - i + 1 > max_len:
                        max_len = j - i + 1
                        start = i
        return s[start:start + max_len]

    def longestPalindrome1(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s
        
        max_len = 1
        res = s[0]
        for i in range(size):
            palindrome_odd, odd_len = self.__center_spread(s, size, i, i)
            palindrome_even, even_len = self.__center_spread(s, size, i, i + 1)

            cur_max_sub = palindrome_odd if odd_len > even_len else palindrome_even
            if len(cur_max_sub) > max_len:
                max_len = len(cur_max_sub)
                res = cur_max_sub
        return res
    
    def __center_spread(self, s, size, left, right):
        i = left
        j = right
        while i >= 0 and j < size and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i + 1:j], j - i - 1
        
# @lc code=end

