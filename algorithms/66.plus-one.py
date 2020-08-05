#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sums = 0
        for i in range(len(digits)):
            sums += 10 ** (len(digits) - 1 - i) * digits[i]
        sums_str = str(sums + 1)
        return [int(j) for j in sums_str]

    def plusOne1(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        ans = [0] * (len(digits) + 1)
        ans[0] = 1
        return ans

    def plusOne2(self, digits: List[int]) -> List[int]:
        return [int(x) for x in str(int(''.join([str(i) for i in digits])) + 1)]


# @lc code=end

