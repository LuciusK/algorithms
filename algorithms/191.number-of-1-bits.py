#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
    
    def hammingWeight1(self, n: int) -> int:
        count = 0
        while n != 0:
            count += 1
            n &= n - 1
        return count


        
# @lc code=end

