class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n < 3:
            return 
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for k in range(n - 2):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            i = k + 1
            j = n - 1
            while i < j:
                sm = nums[k] + nums[i] + nums[j]
                if abs(sm - target) < abs(ans - target):
                    ans = sm
                if sm < target:
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    i += 1
                elif sm > target:
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    j -= 1
                else:
                    return ans
        return ans