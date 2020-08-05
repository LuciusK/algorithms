#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        d = [" ", "*", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []

        def dfs(tmp, index):
            if index == len(digits):
                res.append(tmp)
                return
            
            c = digits[index]
            letters = d[ord(c) - 48]

            for i in letters:
                dfs(tmp+i, index+1)
        
        dfs("", 0)
        return res

    def letterCombinations1(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        d = [" ", "*", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = [""]

        for i in digits:
            size = len(res)
            letters = d[ord(i) - 48]
            for _ in range(size):
                tmp = res.pop(0)
                for j in letters:
                    res.append(tmp+j)
        
        return res

        
# @lc code=end

