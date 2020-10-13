#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = lambda i: points[i][0] ** 2 + points[i][1] ** 2
        def work(i, j, K):
            if i >= j:
                return 
            oi, oj = i, j 
            pivot = dist(i)
            basePoint = points[i]
            while i < j:
                while i < j and dist(j) >= pivot:
                    j -= 1
                points[i] = points[j]
                while i < j and dist(i) <= pivot:
                    i += 1
                points[j] = points[i]
            points[i] = basePoint
            
            if K < i + 1 - oi:
                work(oi, i - 1, K)
            else:
                work(i + 1, oj, K - (i + 1 - oi))
        work(0, len(points) - 1, K)
        return points[:K]
        
# @lc code=end

