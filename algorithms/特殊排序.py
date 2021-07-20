# 计数排序
def countingSort(nums):
    bucket = [0] * (max(nums) + 1)
    for num in nums:
        bucket[num] += 1
    i = 0
    for j in range(len(bucket)):
        while bucket[j] > 0:
            nums[i] = j
            bucket[j] -= 1
            i += 1
    return nums


# 桶排序
def bucketSort(nums, defaultBucketSize=5):
    maxVal, minVal = max(nums), min(nums)
    bucketSize = defaultBucketSize
    bucketcount = (maxVal - minVal) // bucketSize + 1
    buckets = []
    for i in range(bucketcount):
        buckets.append([])
    for num in nums:
        buckets[(num - minVal) // bucketSize].append(num)
    nums.clear()
    for bucket in buckets:
        insertionSort(bucket)
        nums.extend(bucket)
    return nums


# 基数排序(从个位开始)
def radixSort(nums):
    mod = 10
    div = 1
    mostBit = len(str(max(nums)))
    buckets = [[]for _ in range(mod)]
    while mostBit:
        for num in nums:
            buckets[num // div % mod].append(num)
        i = 0
        for bucket in buckets:
            while bucket:
                nums[i] = bucket.pop(0)
                i += 1
        div *= 10
        mostBit -= 1
    return nums