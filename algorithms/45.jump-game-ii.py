#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        maxPosition = 0 # 能力最大范围
        steps = 0
        for i in range(len(nums) - 1): # 不取最后一位是因为不让下面i==end的条件成立，也就是不让steps再加1
            maxPosition = max(maxPosition, nums[i] + i) # i以及之前所有能达到的最远位置
            if i == end: # 到了倒数第二个位置之后，因为非空限制，肯定能到最后一个位置
                end = maxPosition # 倘若到了倒数第二位都没有更新end，那也不用再更新了，因为max一定大于等于最后一位
                steps += 1
        return steps
        
# @lc code=end 