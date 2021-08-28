def mergeSort(nums, left, right):
    if right <= left:
        return
    
    mid = (left + right) >> 1
    mergeSort(nums, left, mid)
    mergeSort(nums, mid + 1, right)
    merge(nums, left, mid, right)

def merge(nums, left, mid, right):
    tmp = []
    i = left
    j = mid + 1
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            tmp.append(nums[i])
            i += 1
        else:
            tmp.append(nums[j])
            j += 1
    while i <= mid:
        tmp.append(nums[i])
        i += 1
    while j <= right:
        tmp.append(nums[j])
        j += 1
    nums[left:right + 1] = tmp

# 递归，分到底了才把数据排序整合
nums = [6,3,1,6,7,4,5,0]
n = len(nums)
mergeSort(nums, 0, n - 1)
print(nums)