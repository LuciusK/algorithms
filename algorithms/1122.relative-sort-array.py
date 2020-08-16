#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr = [0 for _ in range(1001)]
        ans = []
        for num1 in arr1:
            arr[num1] += 1
        for num2 in arr2:
            while arr[num2] > 0:
                ans.append(num2)
                arr[num2] -= 1
        for i in range(len(arr)):
            while arr[i] > 0:
                ans.append(i)
                arr[i] -= 1
        return ans



        
# @lc code=end

