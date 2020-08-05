#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1
        
        start = 0
        end = len(nums) - 1

        while start <= end:#等于可以直接运行下面那段，找到值
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] < nums[end]:#若后面有序
                if nums[mid] < target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:#若前面有序
                if nums[mid] > target and target >= nums[start]:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1 



        
# @lc code=end

