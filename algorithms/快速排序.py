

def quickSort(begin, end, nums):
    if begin >= end:
        return 
    
    pivot_index = partition(begin, end, nums)
    quickSort(begin, pivot_index - 1, nums)
    quickSort(pivot_index + 1, end, nums)

def partition(begin, end, nums):
    pivot = nums[begin]
    mark = begin
    for i in range(begin + 1, end + 1):
        if nums[i] < pivot:
            mark += 1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[begin], nums[mark] = nums[mark], nums[begin]
    return mark