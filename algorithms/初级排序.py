# 冒泡排序
# 遍历数组，每次都相互比较，直到把大的数沉到数组尾部
def bubbleSort(nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


# 选择排序
# 遍历数组，找到最小的值，记录其下标，然后和最初值交换
def selectionSort(nums):
    n = len(nums)
    for i in range(n - 1):
        minIndex = i
        for j in range(i + 1, n):
            if nums[j] < nums[minIndex]:
                minIndex = j
        nums[i], nums[minIndex] = nums[minIndex], nums[i]
    return nums


# 插入排序
# 遍历数组，相互比较元素，小的被一步步往前交换
def insertionSort(nums):
    n = len(nums)
    for i in range(1, n):
        while i > 0 and nums[i - 1] > nums[i]:
            nums[i - 1] , nums[i] = nums[i], nums[i - 1]
            i -= 1
    return nums


# 希尔排序
# 插入排序提升版
def shellSort(nums):
    n = len(nums)
    gap = n // 2
    while gap:
        for i in range(gap, n):
            while i - gap >= 0 and nums[i - gap] > nums[i]:
                nums[i - gap], nums[i] = nums[i], nums[i - gap]
                i -= gap
        gap //= 2
    return nums