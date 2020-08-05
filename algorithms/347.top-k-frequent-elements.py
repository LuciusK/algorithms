#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
import collections
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key = count.get)

    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        return [item[0] for item in collections.Counter(nums).most_common(k)]

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        lookup = Counter(nums)
        heap = []
        for ky, vl in lookup.items():
            heapq.heappush(heap, [-vl, ky])
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

    def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        c = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]#全部都为一个元素就len(nums)

        for x, y in c.items():
            buckets[y].append(x)
        res = []
        for i in range(len(nums), -1, -1):
            if len(res) > k:
                break
            res.extend(buckets[i])
        return res[:k]


# @lc code=end

