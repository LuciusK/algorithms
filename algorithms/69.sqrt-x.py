#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        left = 1
        right = x // 2#一般来说大于4的数，其二分之一的平方都小于他本身

        while left < right:
            mid = (left + right + 1) >> 1#使用右中位数会防止进入死循环
            square = mid * mid

            if square > x:#一步步紧逼目标数，直到取得square稍微小于等于目标数的数
                right = mid - 1
            else:
                left = mid
        return left
    
    def mySqrt1(self, x: int) -> int:#可以使用牛顿迭代法的原因是平方根是x²-a的解
        if x < 0:
            raise Exception('不能输入负数')
        if x == 0:
            return 0
        
        cur = 1
        while True:#迭代公式为x = x - f(x)/f'(x)
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1e-6:
                return int(cur)


        
# @lc code=end

