import random
from typing import List

nums = [9,4,3,2,6]
def sortArray(nums: List[int]) -> List[int]:
    n = len(nums)

    def quick(left, right):
        if left >= right:
            return nums

        # 如果需要变成随机的快速排序，就加入下面两行
        t = random.randint(left, right) # 生成[left,right]之间的一个随机数
        nums[t], nums[left] = nums[left], nums[t]

        pivot = left 
        i = left 
        j = right
        while i < j:
            while i < j and nums[j] > nums[pivot]:
                j -= 1
            while i < j and nums[i] <= nums[pivot]:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[pivot], nums[j] = nums[j], nums[pivot]
        quick(left, j - 1)
        quick(j + 1, right)
        return nums
    return quick(0, n - 1)

print(sortArray(nums))