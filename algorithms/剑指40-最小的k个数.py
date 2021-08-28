import heapq
class Solution:
    def getLeastNumbers1(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()
        
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans

    def getLeastNumbers2(self, arr: List[int], k: int) -> List[int]:
        if k <= 0 or k > len(arr):
            return []
        
        heap = self.build_heap(arr[:k])

        for i in range(k, len(arr)):
            if arr[i] < heap[0]:
                heap[0] = arr[i]
                self.sink(heap, 0)
        return heap

    def sink(self, array, k):
        n = len(array)
        left = 2 * k + 1
        right = 2 * k + 2
        if left >= n: 
            return
        max_i = left
        if right < n and array[left] < array[right]:
            max_i = right
        if array[max_i] > array[k]:
            array[max_i], array[k] = array[k], array[max_i]
            self.sink(array, max_i)
        
    def build_heap(self, list_):
        n = len(list_)
        for i in range(n // 2 - 1, -1, -1):
            self.sink(list_, i)
        return list_

    def getLeastNumbers3(self, arr: List[int], k: int) -> List[int]:
        if k > len(arr) or k <= 0:
            return []
        
        start = 0
        end = len(arr) - 1
        index = self.quickSort(arr, start, end)
        while index != k - 1:
            if index > k - 1:
                end = index - 1
                index = self.quickSort(arr, start, end)
            if index < k - 1:
                start = index + 1
                index = self.quickSort(arr, start, end)
        return arr[:k]

    def quickSort(self, arr, start, end):
        low = start
        high = end
        tmp = arr[start]
        while low < high:
            while low < high and arr[high] >= tmp:
                high -= 1
            arr[low] = arr[high]
            while low < high and arr[low] < tmp:
                low += 1
            arr[high] = arr[low]
        arr[low] = tmp
        return low