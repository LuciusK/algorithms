#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l < r: #最后l肯定等于r
            mid = (l + r + 1) >> 1
            if mid * mid > num:
                r = mid - 1
            else:
                l = mid
        return l * l == num

    def isPerfectSquare1(self, num: int) -> bool:
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0

    def isPerfectSquare2(self, num: int) -> bool:
        i = num
        while i * i > num:
            i = (i + num / i) // 2 #取整只会导致两个结果，要么等于平方根，要么小于平方根，所以不用int(abs)差值
        return i * i == num
            


        
# @lc code=end

