#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        sc = Counter(secret)
        gc = Counter(guess)
        t = sum(x == y for x, y in zip(secret, guess))
        return "{}A{}B".format(t, sum((sc & gc).values()) - t)
        
# @lc code=end

