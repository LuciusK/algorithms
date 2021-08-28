class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        res = ''
        for i in range(n):
            if nums[i][i] == '0':
                res += '1'
            else:
                res += '0'
        return res